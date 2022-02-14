let host = 'http://gateway-n1-dataworks.guazi-cloud.com/api';

/* 需通过美杜莎进行配置, 此环境变量才能生效 */
if (process.env.REACT_APP_ENV === 'production') {
    host = 'https://sso.guazi-apps.com';
}

export const EXAMPLE = {};
export const HOST = host;
