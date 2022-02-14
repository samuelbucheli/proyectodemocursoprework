import { action, observable } from 'mobx';

export default class Header {
    @observable
    content = '';

    @action
    setContent(content: string) {
        this.content = content;
    }

    resetAllState() {
        this.setContent('');
    }
}
