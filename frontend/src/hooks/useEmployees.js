import { useState, useEffect } from 'react'
import { employeeAPI } from '../api/employees'

export const useEmployees = (skip = 0, limit = 10) => {
  const [employees, setEmployees] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [total, setTotal] = useState(0)

  const fetchEmployees = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await employeeAPI.getAll(skip, limit)
      setEmployees(response.data.items)
      setTotal(response.data.total)
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to fetch employees')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchEmployees()
  }, [skip, limit])

  return { employees, loading, error, total, refetch: fetchEmployees }
}

export const useEmployee = (id) => {
  const [employee, setEmployee] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    if (!id) return

    const fetchEmployee = async () => {
      setLoading(true)
      setError(null)
      try {
        const response = await employeeAPI.getById(id)
        setEmployee(response.data)
      } catch (err) {
        setError(err.response?.data?.detail || 'Failed to fetch employee')
      } finally {
        setLoading(false)
      }
    }

    fetchEmployee()
  }, [id])

  return { employee, loading, error }
}

export const useStats = () => {
  const [stats, setStats] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchStats = async () => {
      setLoading(true)
      setError(null)
      try {
        const response = await employeeAPI.getStats()
        setStats(response.data)
      } catch (err) {
        setError(err.response?.data?.detail || 'Failed to fetch statistics')
      } finally {
        setLoading(false)
      }
    }

    fetchStats()
  }, [])

  return { stats, loading, error }
}
