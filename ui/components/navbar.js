import PropTypes from 'prop-types';

import React from 'react';
import SearchContainer from './search/search';
import { Link } from '../routes';

export default function Navbar({ showSearch }) {
  let searchContainer;
  if (showSearch) {
    searchContainer = <SearchContainer />;
  }

  return (
    <div className="overflow-auto">
      <div className="flex items-center navbar">
        <img
          className="pl2 pr1"
          alt="US flag"
          width="50"
          height="50"
          src="/static/img/omb-logo.png"
        />
        <Link route="homepage">
          <a className="text-decoration-none">
            <h1 className="navbar-title">
                OMB Policy Library <sup>BETA</sup>
            </h1>
          </a>
        </Link>
        { searchContainer }
      </div>
    </div>
  );
}

Navbar.propTypes = {
  showSearch: PropTypes.bool,
};

Navbar.defaultProps = {
  showSearch: true,
};
