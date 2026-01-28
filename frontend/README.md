# Employee Management System - Frontend

A modern React frontend for the Employee Management System API.

## Features

- ✅ Employee CRUD operations
- ✅ Department filtering
- ✅ Employee statistics dashboard
- ✅ Pagination support
- ✅ Form validation
- ✅ Toast notifications
- ✅ Responsive design
- ✅ Modern UI with Tailwind CSS

## Tech Stack

- **React** 18.2.0
- **Vite** - Fast build tool
- **Tailwind CSS** - Utility-first CSS
- **Axios** - HTTP client
- **React Router** - Navigation
- **React Icons** - Icon library
- **React Toastify** - Notifications

## Installation

```bash
cd frontend
npm install
```

## Development

```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## Build

```bash
npm run build
```

## Project Structure

```
frontend/
├── src/
│   ├── api/
│   │   ├── client.js          # Axios client
│   │   └── employees.js       # Employee API calls
│   ├── components/
│   │   ├── Navbar.jsx         # Navigation bar
│   │   ├── EmployeeForm.jsx   # Employee form
│   │   ├── EmployeeTable.jsx  # Employee table
│   │   └── StatCard.jsx       # Statistics card
│   ├── hooks/
│   │   └── useEmployees.js    # Custom hooks
│   ├── pages/
│   │   ├── EmployeesPage.jsx  # Employees list page
│   │   └── DashboardPage.jsx  # Dashboard page
│   ├── App.jsx                # Main app component
│   ├── main.jsx               # Entry point
│   └── index.css              # Global styles
├── index.html
├── vite.config.js
├── tailwind.config.js
├── postcss.config.js
└── package.json
```

## API Integration

The frontend connects to the FastAPI backend at `http://localhost:8000/api/v1`

### Available Endpoints

- `GET /employees` - List employees
- `POST /employees` - Create employee
- `GET /employees/{id}` - Get employee
- `PUT /employees/{id}` - Update employee
- `DELETE /employees/{id}` - Delete employee
- `GET /employees/department/{department}` - Filter by department
- `GET /employees/active/list` - Get active employees
- `GET /stats` - Get statistics

## Features

### Employees Page
- View all employees in a table
- Create new employees
- Edit existing employees
- Delete employees
- Pagination support
- Form validation

### Dashboard Page
- Total employees count
- Active/inactive employees
- Average salary
- Department breakdown
- Total payroll
- Active rate percentage

## Configuration

The API base URL is configured in `src/api/client.js`:

```javascript
const API_BASE_URL = 'http://localhost:8000/api/v1'
```

Change this if your backend is running on a different URL.

## Styling

The project uses Tailwind CSS for styling. Custom styles are defined in `src/index.css`.

### Custom Classes

- `.btn` - Base button style
- `.btn-primary` - Primary button
- `.btn-secondary` - Secondary button
- `.btn-danger` - Danger button
- `.btn-success` - Success button
- `.card` - Card container
- `.input-field` - Input field
- `.table-row` - Table row

## Error Handling

The application includes error handling for:
- Network errors
- Validation errors
- Server errors
- Not found errors

Errors are displayed as toast notifications.

## Performance

- Lazy loading of components
- Pagination for large datasets
- Efficient API calls
- Optimized re-renders

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Future Enhancements

1. Authentication
2. Advanced search and filtering
3. Export to CSV/PDF
4. Bulk operations
5. Employee profiles
6. Performance charts
7. Dark mode
8. Multi-language support

## Troubleshooting

### Port Already in Use

Change the port in `vite.config.js`:

```javascript
server: {
  port: 3001,
  // ...
}
```

### API Connection Error

Ensure the backend is running at `http://localhost:8000`

Check the API base URL in `src/api/client.js`

### Build Errors

Clear node_modules and reinstall:

```bash
rm -rf node_modules
npm install
npm run build
```

## License

MIT
