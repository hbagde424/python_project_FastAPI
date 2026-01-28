import React from 'react'
import { FaEdit, FaTrash, FaSpinner } from 'react-icons/fa'
import { employeeAPI } from '../api/employees'
import { toast } from 'react-toastify'

export default function EmployeeTable({ employees, loading, onEdit, onDelete }) {
  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this employee?')) {
      try {
        await employeeAPI.delete(id)
        toast.success('Employee deleted successfully!')
        onDelete()
      } catch (error) {
        toast.error('Failed to delete employee')
      }
    }
  }

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <FaSpinner className="animate-spin text-4xl text-blue-600" />
      </div>
    )
  }

  if (employees.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500 text-lg">No employees found</p>
      </div>
    )
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full">
        <thead className="bg-gray-100 border-b-2 border-gray-300">
          <tr>
            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Name</th>
            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Email</th>
            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Position</th>
            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Department</th>
            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Salary</th>
            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Status</th>
            <th className="px-6 py-3 text-left text-sm font-semibold text-gray-700">Actions</th>
          </tr>
        </thead>
        <tbody>
          {employees.map(employee => (
            <tr key={employee.id} className="table-row">
              <td className="px-6 py-4 text-sm text-gray-900">{employee.name}</td>
              <td className="px-6 py-4 text-sm text-gray-600">{employee.email}</td>
              <td className="px-6 py-4 text-sm text-gray-600">{employee.position}</td>
              <td className="px-6 py-4 text-sm text-gray-600">{employee.department}</td>
              <td className="px-6 py-4 text-sm text-gray-900 font-medium">
                ${employee.salary.toLocaleString()}
              </td>
              <td className="px-6 py-4 text-sm">
                <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                  employee.is_active 
                    ? 'bg-green-100 text-green-800' 
                    : 'bg-red-100 text-red-800'
                }`}>
                  {employee.is_active ? 'Active' : 'Inactive'}
                </span>
              </td>
              <td className="px-6 py-4 text-sm">
                <div className="flex gap-2">
                  <button
                    onClick={() => onEdit(employee)}
                    className="text-blue-600 hover:text-blue-800 transition-colors"
                    title="Edit"
                  >
                    <FaEdit />
                  </button>
                  <button
                    onClick={() => handleDelete(employee.id)}
                    className="text-red-600 hover:text-red-800 transition-colors"
                    title="Delete"
                  >
                    <FaTrash />
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
