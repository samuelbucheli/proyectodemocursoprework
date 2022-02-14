import axios, { AxiosRequestConfig, Canceler, Method } from 'axios';
import { message } from 'antd';
import { HTTP_METHOD } from '@/const/http';

axios.defaults.withCredentials = true;
axios.interceptors.request.use(
    config => {
        return config;
    },
    err => {
        return Promise.reject(err);
    }
);

axios.interceptors.response.use(
    response => {
        return response;
    },
    error => {
        return Promise.reject(error);
    }
);

interface AnyObj {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    [propName: string]: any;
}

interface Res {
    message: string;
    success: boolean;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    data: any;
}

/**
 * 是否需要cancel之前未完成的请求
 * 只针对返回值为上述Res类型的请求
 */
export function createFetch(needCancel?: boolean) {
    const { CancelToken } = axios;
    let cancel: Canceler | null;

    return function fetch(
        url: string,
        method?: Method,
        data?: AnyObj | string,
        config = {} as AxiosRequestConfig
    ) {
        if (cancel) {
            cancel('cancel pre request');
        }

        const options: AxiosRequestConfig = {
            cancelToken: needCancel
                ? new CancelToken(function executor(c) {
                      cancel = c;
                  })
                : undefined,
            method: method || HTTP_METHOD.GET,
            url,
            ...config
        };

        if (method === HTTP_METHOD.POST) {
            options.data = data;
        }

        if (options.method === HTTP_METHOD.GET) {
            options.params = data;
        }

        return new Promise((resolve, reject) => {
            axios(options)
                .then(res => {
                    const {
                        message: msg,
                        data: resData,
                        success
                    } = res.data as Res;
                    if (!success) {
                        message.error(msg || '未知错误');
                        Promise.reject(res.data);
                    } else {
                        resolve(resData);
                    }
                })
                .catch(err => {
                    reject(err);
                });
        });
    };
}

export default axios;
