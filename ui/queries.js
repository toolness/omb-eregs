import moment from 'moment';
import PropTypes from 'prop-types';
import validator from 'validator';

import api from './api';
import { apiNameField, search } from './lookup-search';
import { routes } from './routes';

const NUM_POLICIES = 4;
// See https://momentjs.com/docs/#/displaying/ for options
const DATE_FORMAT = 'MMMM D, YYYY';


export function formatIssuance(policy) {
  return Object.assign({}, policy, {
    issuance_pretty: moment(policy.issuance).format(DATE_FORMAT),
  });
}

export async function homepageData() {
  const results = await api.policies.fetchResults({ ordering: '-issuance' });
  return {
    recentPolicies: results.slice(0, NUM_POLICIES).map(formatIssuance),
  };
}

export async function policiesData({ query }) {
  const results = await Promise.all([
    api.topics.withIds(query.requirements__all_agencies__id__in),
    api.policies.withIds(query.id__in),
    api.topics.withIds(query.requirements__topics__id__in),
    api.policies.fetch(Object.assign({ ordering: 'policy_number' }, query)),
  ]);
  return {
    existingAgencies: results[0],
    existingPolicies: results[1],
    existingTopics: results[2],
    pagedPolicies: results[3],
  };
}

export async function requirementsData({ query }) {
  const results = await Promise.all([
    api.topics.withIds(query.all_agencies__id_in),
    api.policies.withIds(query.policy__id__in),
    api.topics.withIds(query.topics__id__in),
    api.requirements.fetch(query),
  ]);
  return {
    existingAgencies: results[0],
    existingPolicies: results[1],
    existingTopics: results[2],
    pagedReqs: results[3],
  };
}


/*
 * We expect a query like
 *  /some/path/?q=term&insertParam=lookup_id__in&page=1
 *    &redirectRoute=/prev/path&redirectQuery__lookup_id__in=1,2,3
 *    &redirectQuery__someOtherParameter=value
 * Return a clean version of that data; if we can't validate, raise an
 * exception.
 */
const redirectQueryPrefix = 'redirectQuery__';
const validRoutes = routes.map(r => r.name).filter(n => n);

function userError(message) {
  const err = new Error(message);
  err.msg = message; // Error's aren't serialized
  err.statusCode = 400;
  return err;
}

export function cleanSearchParams(query) {
  const clean = {
    q: (query.q || '').toString(),
    insertParam: (query.insertParam || '').toString(),
    lookup: (query.lookup || '').toString(),
    redirect: {
      route: (query.redirectRoute || '').toString(),
      query: {},
    },
    page: (query.page || '1').toString(),
  };
  Object.keys(query).forEach((key) => {
    if (key.startsWith(redirectQueryPrefix)) {
      clean.redirect.query[key.substring(redirectQueryPrefix.length)] = query[key];
    }
  });

  if (validator.isEmpty(clean.insertParam)) {
    throw userError('Needs an "insertParam" parameter');
  } else if (!validator.isIn(clean.redirect.route, validRoutes)) {
    throw userError('Invalid "redirectRoute" parameter');
  } else if (!validator.isIn(clean.lookup, Object.keys(apiNameField))) {
    throw userError('Invalid "lookup" parameter');
  }

  return clean;
}
export const cleanSearchParamTypes = PropTypes.shape({
  q: PropTypes.string.isRequired,
  insertParam: PropTypes.string.isRequired,
  lookup: PropTypes.oneOf(Object.keys(apiNameField)).isRequired,
  redirect: PropTypes.shape({
    route: PropTypes.string.isRequired,
    query: PropTypes.shape({}).isRequired,
  }).isRequired,
});

export async function searchRedirectData({ query }) {
  const userParams = cleanSearchParams(query);
  const pagedEntries = await search(
    userParams.lookup, userParams.q, userParams.page);
  return { pagedEntries, userParams };
}