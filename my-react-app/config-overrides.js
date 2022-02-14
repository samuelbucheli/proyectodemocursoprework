const {
    override,
    fixBabelImports,
    addWebpackAlias,
    addLessLoader,
    useEslintRc,
} = require('customize-cra');
const path = require('path');
const fs = require('fs');
const HtmlWebpackPlugin = require('html-webpack-plugin');

/* rewrite cra 默认地址 */
const paths = require('react-scripts/config/paths');
if (process.env.REACT_APP_MP) {
    paths.appIndexJs = `${paths.appSrc}/pages/index.tsx`;
    paths.servedPath = './';
}

/* 多入口配置 */
const getEntryConfig = env => {
    const arr =
        'development' === env
            ? [require.resolve('react-dev-utils/webpackHotDevClient')]
            : [];
    return entry => {
        return [...arr, `${paths.appSrc}/pages/${entry}.tsx`];
    };
};

const removePlugin = (plugins, name) => {
    const list = plugins.filter(
        it =>
            !(
                it.constructor &&
                it.constructor.name &&
                name === it.constructor.name
            )
    );
    if (list.length === plugins.length) {
        throw new Error(`Can not found plugin: ${name}.`);
    }
    return list;
};

const genHtmlWebpackPlugin = env => {
    const minify = {
        removeComments: true,
        collapseWhitespace: true,
        removeRedundantAttributes: true,
        useShortDoctype: true,
        removeEmptyAttributes: true,
        removeStyleLinkTypeAttributes: true,
        keepClosingSlash: true,
        minifyJS: true,
        minifyCSS: true,
        minifyURLs: true,
    };
    const config = Object.assign(
        {},
        { inject: true, template: paths.appHtml },
        'development' !== env ? { minify } : undefined
    );
    return entry => {
        return new HtmlWebpackPlugin({
            ...config,
            chunks: ['vendors', `runtime~${entry}`, entry],
            filename: `${entry}.html`,
        });
    };
};

const getPageList = () => {
    const files = fs.readdirSync(path.resolve(__dirname, './src/pages'));
    return files
        .filter(file => /\.tsx$/.test(file))
        .map(file => file.replace('.tsx', ''));
};

const supportMultiPage = (config, env) => {
    if (!process.env.REACT_APP_MP) {
        return config;
    }
    const list = getPageList();
    config.entry = {};
    config.plugins = removePlugin(config.plugins, 'HtmlWebpackPlugin');
    const getEntry = getEntryConfig(env);
    const getHtmlWebpackPlugin = genHtmlWebpackPlugin(env);
    list.forEach(it => {
        config.entry[it] = getEntry(it);
        config.plugins.push(getHtmlWebpackPlugin(it));
    });

    if ('development' === env) {
        config.output.filename = 'static/js/[name].bundle.js';
    }

    return config;
};

module.exports = {
    webpack: override(
        supportMultiPage,
        fixBabelImports('import', {
            libraryName: 'antd',
            libraryDirectory: 'es',
            style: true,
        }),
        addLessLoader({
            javascriptEnabled: true,
            globalVars: {
                '@main-color': 'rgba(0, 0, 0, .85)',
            },
            paths: [
                path.resolve(__dirname, 'src/'),
                path.resolve(__dirname, 'src/views/'),
            ],
        }),
        addWebpackAlias({
            ['mock']: path.resolve(__dirname, 'src/mock/'),
            ['@']: path.resolve(__dirname, 'src/'),
            ['views']: path.resolve(__dirname, 'src/views/'),
        }),
        useEslintRc()
    ),
    devServer: configFunction => {
        return (proxy, allowedHost) => {
            const config = configFunction(proxy, allowedHost);
            return config;
        };
    },
};
