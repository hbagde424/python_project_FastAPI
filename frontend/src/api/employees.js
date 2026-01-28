import client from './client'

export const employeeAPI = {
  // Get all employees
  getAll: (skip = 0, limit = 10) => {
    return client.get('/employees', {
      params: { skip, limit }
    })
  },

  // Get single employee
  getById: (id) => {
    return client.get(`/employees/${id}`)
  },

  // Create employee
  create: (data) => {
    return client.post('/employees', data)
  },

  // Update employee
  update: (id, data) => {
    return client.put(`/employees/${id}`, data)
  },

  // Delete employee
  delete: (id) => {
    return client.delete(`/employees/${id}`)
  },

  // Get employees by department
  getByDepartment: (department, skip = 0, limit = 10) => {
    return client.get(`/employees/department/${department}`, {
      params: { skip, limit }
    })
  },

  // Get active employees
  getActive: (skip = 0, limit = 10) => {
    return client.get('/employees/active/list', {
      params: { skip, limit }
    })
  },

  // Get statistics
  getStats: () => {
    return client.get('/stats')
  }
}
