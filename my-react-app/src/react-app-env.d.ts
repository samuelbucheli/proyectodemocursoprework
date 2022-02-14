/// <reference types="react-scripts" />

/* 此处是在ts中使用less的module形式 */
declare module '*.module.less' {
    const classes: {
        [key: string]: string
    };
    export default classes;
}
