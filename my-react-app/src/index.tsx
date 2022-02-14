import React from 'react';
import ReactDOM from 'react-dom';
import { configure } from 'mobx';
import { Provider } from 'mobx-react';
import { BrowserRouter as Router } from 'react-router-dom';
import { LocaleProvider } from 'antd';
import moment from 'moment';
import 'moment/locale/zh-cn';
import znCN from 'antd/lib/locale-provider/zh_CN';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import store from './store';

import 'normalize.css';

/* mobx-config */
configure({ enforceActions: 'observed' });
moment.locale('zh-cn');

ReactDOM.render(
    <LocaleProvider locale={znCN}>
        <Provider {...store}>
            <Router>
                <App />
            </Router>
        </Provider>
    </LocaleProvider>,
    document.getElementById('root') as HTMLElement
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
