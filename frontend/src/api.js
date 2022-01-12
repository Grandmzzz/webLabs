import Axios from "axios";

const axiosConfig = {
    baseURL: 'http://127.0.0.1:8000/api',
    timeout: 30000
};
export const axios = Axios.create(axiosConfig);

export const returnData = responce => responce.data


export function authRequest(userData, url) {
    return axios
        .post(`/auth/${url}`, userData)
        .then(returnData)
}

export const login = userData => authRequest(userData, 'login')

export function register(userData) {
    return authRequest(userData, 'registration')
}


export const articleRequest = (url, params) => {
    return axios
        .get(`/articles/${url}`, {params})
        .then(returnData)
}

export const getArticle = articleId => articleRequest(`feed/${articleId}`, {})

export const getHome = () => articleRequest('feed', {})

export const getTags = () => articleRequest('tag', {})

export const search = search_text => articleRequest('feed/by_text', {search_text})