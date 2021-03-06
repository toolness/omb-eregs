import { shallow } from 'enzyme';
import React from 'react';

import Req from '../../../components/policy/req';

describe('<Req />', () => {
  const req = {
    req_id: '123.45',
    req_text: 'Some text here',
    topics: [],
    policy: [],
  };

  it('includes meta data when highlighted', () => {
    const normalText = shallow(
      <Req href="" onClick={jest.fn()} req={req} />,
    ).html();
    const hlText = shallow(
      <Req highlighted href="" onClick={jest.fn()} req={req} />,
    ).html();

    expect(normalText).toMatch(/Some text here/);
    expect(normalText).not.toMatch(/>123.45</);
    expect(hlText).toMatch(/Some text here/);
    expect(hlText).toMatch(/Requirement ID: 123.45/);
  });

  it('includes topiclinks with data when highlighted', () => {
    const topiclinksReq = { ...req, topics: [{ id: 1, name: 'link 1' }, { id: 2, name: 'link 2' }] };
    const normalText = shallow(
      <Req highlighted href="" onClick={jest.fn()} req={topiclinksReq} />,
    ).find('.topics').html();

    expect(normalText).toMatch(/link 1/);
    expect(normalText).toMatch(/link 2/);
  });

  it('includes an anchor with the correct data', () => {
    const onClick = jest.fn();
    const anchorReq = { ...req, req_id: '1.1', req_text: 'Text goes here' };
    const anchors = shallow(
      <Req href="/some/location" onClick={onClick} req={anchorReq} />,
    ).find('a');
    expect(anchors).toHaveLength(1);

    const anchor = anchors.first();
    expect(anchor.prop('href')).toEqual('/some/location');
    expect(anchor.prop('onClick')).toBe(onClick);
  });
});
