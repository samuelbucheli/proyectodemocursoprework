import Example from './example';

export interface Store {
    example: Example;
}

const store = {
    example: new Example()
};
export default store;
