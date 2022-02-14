const colors = [
    '#0000CC',
    '#0099CC',
    '#0099FF',
    '#00CC00',
    '#00CCCC',
    '#00CCFF',
    '#3300CC',
    '#3300FF',
    '#3333CC',
    '#3333FF',
    '#3366CC',
    '#3366FF',
    '#3399CC',
    '#3399FF',
    '#33CC00',
    '#33CC33',
    '#33CC66',
    '#33CC99',
    '#33CCCC',
    '#33CCFF',
    '#6600CC',
    '#6600FF',
    '#6633CC',
    '#6633FF',
    '#66CC00',
    '#66CC33',
    '#9900CC',
    '#9900FF',
    '#9933CC',
    '#9933FF',
    '#99CC00',
    '#99CC33',
    '#CC0000',
    '#CC0033',
    '#CC0066',
    '#CC0099',
    '#CC00CC',
    '#CC00FF',
    '#CC3300',
    '#CC3333',
    '#CC3366',
    '#CC3399',
    '#CC33CC',
    '#CC33FF',
    '#CC6600',
    '#CC6633',
    '#CC9900',
    '#CC9933',
    '#CCCC00',
    '#CCCC33',
    '#FF0000',
    '#FF0033',
    '#FF0066',
    '#FF0099',
    '#FF00CC',
    '#FF00FF',
    '#FF3300',
    '#FF3333',
    '#FF3366',
    '#FF3399',
    '#FF33CC',
    '#FF33FF',
    '#FF6600',
    '#FF6633',
    '#FF9900',
    '#FF9933',
    '#FFCC00',
    '#FFCC33'
];
let colorIndex = 0;
const isDevelopMod = process.env.NODE_ENV === 'development';

/**
 * 简单的debug工具，用于区分debug的来源
 * 以及在发布模式的时候，隐藏debug内容
 * @param {String} namespace debug的命名空间
 */
function debug(namespace: string) {
    const color = colors[colorIndex];
    colorIndex += 1;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    return (...debugArgs: any) => {
        if (isDevelopMod) {
            // eslint-disable-next-line no-console
            console.log(`%c ${namespace}: `, `color: ${color}`, ...debugArgs);
        }
    };
}

export default debug;
