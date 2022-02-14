import { Method } from 'axios';

export const HTTP_RESPONSE_STATE = {
    ERROR: 10002,
    SUCCESS: 200

    // Others failure state
};

export const HTTP_RESPONSE_STATUS = {
    SUCCESS: 200,
    SUCCESS_CEILING: 300,
    // Others failure state

    UNAUTHORIZED: 401,
    FORBIDDEN: 403,
    NOT_FOUND: 404
};

type HttpMethod = {
    [propName in Method]: propName;
};

export const HTTP_METHOD: HttpMethod = {
    get: 'get',
    GET: 'GET',
    delete: 'delete',
    DELETE: 'DELETE',
    head: 'head',
    HEAD: 'HEAD',
    options: 'options',
    OPTIONS: 'OPTIONS',
    post: 'post',
    POST: 'POST',
    put: 'put',
    PUT: 'PUT',
    patch: 'patch',
    PATCH: 'PATCH'
};
