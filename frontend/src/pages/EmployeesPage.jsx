import React, { useState } from 'react'
import { FaPlus } from 'react-icons/fa'
import { useEmployees } from '../hooks/useEmployees'
import EmployeeTable from '../components/EmployeeTable'
import EmployeeForm from '../components/EmployeeForm'

export default function EmployeesPage() {
  const [showForm, setShowForm] = useState(false)
  const [selectedEmployee, setSelectedEmployee] = useState(null)
  const [skip, setSkip] = useState(0)
  const limit = 10

  const { employees, loading, error, total, refetch } = useEmployees(skip, limit)

  const handleEdit = (employee) => {
    setSelectedEmployee(employee)
    setShowForm(true)
  }

  const handleSuccess = () => {
    setShowForm(false)
    setSelectedEmployee(null)
    refetch()
  }

  const handleCancel = () => {
    setShowForm(false)
    setSelectedEmployee(null)
  }

  const totalPages = Math.ceil(total / limit)
  const currentPage = Math.floor(skip / limit) + 1

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Employees</h1>
        {!showForm && (
          <button
            onClick={() => setShowForm(true)}
            className="btn-primary flex items-center gap-2"
          >
            <FaPlus /> Add Employee
          </button>
        )}
      </div>

      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-4">
          {error}
        </div>
      )}

      {showForm && (
        <div className="card mb-8">
          <h2 className="text-xl font-bold mb-4">
            {selectedEmployee ? 'Edit Employee' : 'Add New Employee'}
          </h2>
          <EmployeeForm
            employee={selectedEmployee}
            onSuccess={handleSuccess}
            onCancel={handleCancel}
          />
        </div>
      )}

      <div className="card">
        <EmployeeTable
          employees={employees}
          loading={loading}
          onEdit={handleEdit}
          onDelete={refetch}
        />

        {/* Pagination */}
        {totalPages > 1 && (
          <div className="flex justify-between items-center mt-6 pt-6 border-t">
            <p className="text-sm text-gray-600">
              Showing {skip + 1} to {Math.min(skip + limit, total)} of {total} employees
            </p>
            <div className="flex gap-2">
              <button
                onClick={() => setSkip(Math.max(0, skip - limit))}
                disabled={skip === 0}
                className="btn-secondary disabled:opacity-50"
              >
                Previous
              </button>
              <span className="px-4 py-2 text-sm font-medium">
                Page {currentPage} of {totalPages}
              </span>
              <button
                onClick={() => setSkip(skip + limit)}
                disabled={skip + limit >= total}
                className="btn-secondary disabled:opacity-50"
              >
                Next
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
