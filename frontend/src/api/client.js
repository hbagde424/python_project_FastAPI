import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api/v1'

const client = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor
client.interceptors.request.use(
  (config) => {
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
client.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 404) {
      console.error('Resource not found')
    } else if (error.response?.status === 400) {
      console.error('Bad request:', error.response.data)
    } else if (error.response?.status === 500) {
      console.error('Server error')
    }
    return Promise.reject(error)
  }
)

export default client
