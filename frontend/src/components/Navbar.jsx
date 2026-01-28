import React from 'react'
import { Link } from 'react-router-dom'
import { FaUsers, FaChartBar } from 'react-icons/fa'

export default function Navbar() {
  return (
    <nav className="bg-blue-600 text-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <Link to="/" className="flex items-center gap-2 text-2xl font-bold">
            <FaUsers />
            Employee Management
          </Link>
          
          <div className="flex gap-6">
            <Link 
              to="/" 
              className="hover:bg-blue-700 px-3 py-2 rounded-md transition-colors"
            >
              Employees
            </Link>
            <Link 
              to="/dashboard" 
              className="hover:bg-blue-700 px-3 py-2 rounded-md transition-colors flex items-center gap-2"
            >
              <FaChartBar />
              Dashboard
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
}
