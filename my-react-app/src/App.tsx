import React from 'react';
import { compose } from 'lodash/fp';
import { withRouter, Route } from 'react-router-dom';
import './App.css';

import Example from '@/views/Example';
import { EXAMPLE, DEFAULT } from './const/route';

function App() {
    return (
        <div className="app-container">
            <Route path={[DEFAULT, EXAMPLE]} component={Example} />
        </div>
    );
}

export default compose(withRouter)(App);
