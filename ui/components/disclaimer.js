import React from 'react';

import Link from './link';

export default function Disclaimer() {
  return (
    <div className="sm-flex justify-between usa-disclaimer">
      <div>
        <img
          className="usa-disclaimer-flag"
          alt="US flag"
          src="/static/img/usa-flag.png"
        />
        An official website of the United States government
      </div>
      <div className="usa-disclaimer-text">
        We&apos;re designing the site and adding policies in phases.
        <br />
        Questions or comments?{' '}
        <Link href="mailto:ofcio@omb.eop.gov">Email ofcio@omb.eop.gov</Link>.
      </div>
    </div>
  );
}
