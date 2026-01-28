import React from 'react'
import { FaUsers, FaCheckCircle, FaTimesCircle, FaMoneyBillWave } from 'react-icons/fa'
import { useStats } from '../hooks/useEmployees'
import StatCard from '../components/StatCard'

export default function DashboardPage() {
  const { stats, loading, error } = useStats()

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p className="text-gray-500">Loading statistics...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-8">
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
          {error}
        </div>
      </div>
    )
  }

  if (!stats) {
    return null
  }

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Dashboard</h1>

      {/* Main Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <StatCard
          title="Total Employees"
          value={stats.total_employees}
          icon={FaUsers}
          color="blue"
        />
        <StatCard
          title="Active Employees"
          value={stats.active_employees}
          icon={FaCheckCircle}
          color="green"
        />
        <StatCard
          title="Inactive Employees"
          value={stats.inactive_employees}
          icon={FaTimesCircle}
          color="orange"
        />
        <StatCard
          title="Average Salary"
          value={`$${stats.average_salary.toLocaleString('en-US', { maximumFractionDigits: 0 })}`}
          icon={FaMoneyBillWave}
          color="purple"
        />
      </div>

      {/* Department Stats */}
      <div className="card">
        <h2 className="text-2xl font-bold mb-6">Department Breakdown</h2>
        
        {Object.keys(stats.departments).length === 0 ? (
          <p className="text-gray-500">No department data available</p>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {Object.entries(stats.departments).map(([dept, data]) => (
              <div key={dept} className="border border-gray-200 rounded-lg p-4">
                <h3 className="font-semibold text-lg text-gray-900 mb-3">{dept}</h3>
                <div className="space-y-2">
                  <div className="flex justify-between">
                    <span className="text-gray-600">Employees:</span>
                    <span className="font-semibold">{data.count}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-600">Avg Salary:</span>
                    <span className="font-semibold">
                      ${data.avg_salary.toLocaleString('en-US', { maximumFractionDigits: 0 })}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Summary */}
      <div className="card mt-8">
        <h2 className="text-2xl font-bold mb-4">Summary</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <p className="text-gray-600 mb-2">Total Payroll</p>
            <p className="text-3xl font-bold text-blue-600">
              ${stats.total_salary.toLocaleString('en-US', { maximumFractionDigits: 0 })}
            </p>
          </div>
          <div>
            <p className="text-gray-600 mb-2">Active Rate</p>
            <p className="text-3xl font-bold text-green-600">
              {stats.total_employees > 0 
                ? ((stats.active_employees / stats.total_employees) * 100).toFixed(1)
                : 0
              }%
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
