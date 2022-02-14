import { observable } from 'mobx';

import Header from './header';
import Main from './main';

export default class Example {
    @observable
    header = new Header();

    @observable
    main = new Main();
}
