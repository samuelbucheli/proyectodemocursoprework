import React, { useState, useEffect } from 'react';
import { compose } from 'lodash/fp';
import { withRouter, Route, Link } from 'react-router-dom';
import { observer } from 'mobx-react';

import Header from './views/Header';
import Main from './views/Main';

import { EXAMPLE_MAIN, EXAMPLE_HEADER, EXAMPLE } from '@/const/route';

function Example() {
    const [count, addCount] = useState(0);
    useEffect(() => {
        setTimeout(() => {
            addCount(count + 1);
        }, 1000);
    }, [count]);

    return (
        <div>
            this is just a example!
            {count}
            <br />
            <Link to={EXAMPLE_HEADER}>to Header</Link>
            <br />
            <Link to={EXAMPLE_MAIN}>to Main</Link>
            {/* 如果需要采用二级路由 */}
            <Route exact path={[EXAMPLE, EXAMPLE_HEADER]} component={Header} />
            <Route exact path={EXAMPLE_MAIN} component={Main} />
        </div>
    );
}

export default compose(
    withRouter,
    observer
)(Example);
