import axios from "axios";

const baseURL = "http://localhost:8000/api/";
const access_token = localStorage.getItem("access_token");
const refresh_token = localStorage.getItem("refresh_token");

export const axiosInstance = axios.create({
  baseURL: baseURL,
  timeout: 5000,
});

axiosInstance.interceptors.request.use((config) => {
  config.headers["Authorization"] = `Bearer ${access_token}`;
  return config;
});

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  async function (error) {
    if (error.response.status === 403 && refresh_token) {
      try {
        const res = await axios.post(
          "http://127.0.0.1:8000/api/token/refresh/",
          {
            refresh: refresh_token,
          }
        );
        localStorage.setItem("access_token", res.data.access);
        localStorage.setItem("refresh_token", res.data.refresh);
        error.config.headers["Authorization"] = `Bearer ${res.data.access}`;
        return axios.request(error.config);
      } catch (error) {
        if (window.location.pathname !== "/register" && window.location.pathname !== "/login") {
          window.location.href = "/login";
          localStorage.removeItem("access_token")
          localStorage.removeItem("refresh_token")
        }
      }
    } else {
      if (window.location.pathname !== "/register" && window.location.pathname !== "/login" ) {
        window.location.href = "/login"; 
        localStorage.removeItem("access_token")
        localStorage.removeItem("refresh_token")
      }
    }
  }
);

export default axiosInstance;
