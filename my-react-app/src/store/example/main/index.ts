import { action, observable } from 'mobx';

export default class Main {
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
