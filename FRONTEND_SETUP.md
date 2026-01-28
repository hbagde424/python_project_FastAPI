# Frontend Setup Guide

## Prerequisites

- Node.js 16+ and npm
- Backend running on http://localhost:8000

## Installation Steps

### 1. Navigate to Frontend Directory

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

This will install all required packages:
- React 18.2.0
- Vite (build tool)
- Tailwind CSS
- Axios
- React Router
- React Icons
- React Toastify

### 3. Start Development Server

```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Project Structure

```
frontend/
├── src/
│   ├── api/
│   │   ├── client.js              # Axios HTTP client
│   │   └── employees.js           # Employee API endpoints
│   ├── components/
│   │   ├── Navbar.jsx             # Navigation component
│   │   ├── EmployeeForm.jsx       # Employee form component
│   │   ├── EmployeeTable.jsx      # Employee table component
│   │   └── StatCard.jsx           # Statistics card component
│   ├── hooks/
│   │   └── useEmployees.js        # Custom React hooks
│   ├── pages/
│   │   ├── EmployeesPage.jsx      # Employees list page
│   │   └── DashboardPage.jsx      # Dashboard page
│   ├── App.jsx                    # Main app component
│   ├── main.jsx                   # React entry point
│   └── index.css                  # Global styles
├── index.html                     # HTML template
├── vite.config.js                 # Vite configuration
├── tailwind.config.js             # Tailwind configuration
├── postcss.config.js              # PostCSS configuration
└── package.json                   # Dependencies
```

## Features

### Pages

#### 1. Employees Page (`/`)
- View all employees in a table
- Create new employees
- Edit existing employees
- Delete employees
- Pagination support
- Form validation

#### 2. Dashboard Page (`/dashboard`)
- Total employees count
- Active/inactive employees
- Average salary
- Department breakdown
- Total payroll
- Active rate percentage

### Components

#### Navbar
- Navigation between pages
- Logo and branding

#### EmployeeForm
- Create/edit employee form
- Form validation
- Error handling
- Success notifications

#### EmployeeTable
- Display employees in table format
- Edit and delete buttons
- Status badges
- Formatted salary display

#### StatCard
- Display statistics
- Customizable colors
- Icon support

### Hooks

#### useEmployees
- Fetch all employees with pagination
- Fetch single employee
- Fetch statistics
- Loading and error states

## API Integration

The frontend connects to the backend API at `http://localhost:8000/api/v1`

### API Endpoints Used

```
GET    /employees                    # List employees
POST   /employees                    # Create employee
GET    /employees/{id}               # Get employee
PUT    /employees/{id}               # Update employee
DELETE /employees/{id}               # Delete employee
GET    /employees/department/{dept}  # Filter by department
GET    /employees/active/list        # Get active employees
GET    /stats                        # Get statistics
```

## Configuration

### API Base URL

Edit `src/api/client.js` to change the API base URL:

```javascript
const API_BASE_URL = 'http://localhost:8000/api/v1'
```

### Development Server Port

Edit `vite.config.js` to change the port:

```javascript
server: {
  port: 3000,
  // ...
}
```

### Tailwind CSS

Customize Tailwind in `tailwind.config.js`:

```javascript
theme: {
  extend: {
    colors: {
      primary: '#3b82f6',
      secondary: '#10b981',
      danger: '#ef4444',
      warning: '#f59e0b',
    }
  },
}
```

## Development Workflow

### 1. Start Backend

```bash
# In the root directory
python run.py
```

### 2. Start Frontend

```bash
# In the frontend directory
npm run dev
```

### 3. Access Application

Open http://localhost:3000 in your browser

### 4. Make Changes

Edit files in `src/` directory. Changes will hot-reload automatically.

## Building for Production

### Build

```bash
npm run build
```

This creates an optimized build in the `dist/` directory.

### Preview Build

```bash
npm run preview
```

This serves the production build locally for testing.

## Deployment

### Option 1: Deploy to Vercel

```bash
npm install -g vercel
vercel
```

### Option 2: Deploy to Netlify

```bash
npm install -g netlify-cli
netlify deploy --prod --dir=dist
```

### Option 3: Deploy to GitHub Pages

1. Update `vite.config.js`:
```javascript
export default defineConfig({
  base: '/employee-management/',
  // ...
})
```

2. Build and deploy:
```bash
npm run build
# Deploy dist/ folder to GitHub Pages
```

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 3000
lsof -i :3000  # macOS/Linux
netstat -ano | findstr :3000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

### API Connection Error

1. Ensure backend is running: `python run.py`
2. Check API URL in `src/api/client.js`
3. Check CORS configuration in backend

### Module Not Found

```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Build Errors

```bash
# Clear Vite cache
rm -rf dist .vite
npm run build
```

## Performance Tips

1. Use React DevTools to identify re-renders
2. Implement code splitting for large components
3. Use lazy loading for routes
4. Optimize images
5. Monitor bundle size with `npm run build`

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Environment Variables

Create a `.env` file in the frontend directory:

```
VITE_API_URL=http://localhost:8000/api/v1
```

Then use in code:

```javascript
const API_BASE_URL = import.meta.env.VITE_API_URL
```

## Testing

### Run Tests

```bash
npm test
```

### Test Coverage

```bash
npm test -- --coverage
```

## Linting

### Run ESLint

```bash
npm run lint
```

### Fix Linting Issues

```bash
npm run lint -- --fix
```

## Next Steps

1. Customize styling in `src/index.css`
2. Add more pages/components as needed
3. Implement authentication
4. Add advanced filtering
5. Implement export functionality
6. Add dark mode support

## Resources

- [React Documentation](https://react.dev)
- [Vite Documentation](https://vitejs.dev)
- [Tailwind CSS Documentation](https://tailwindcss.com)
- [Axios Documentation](https://axios-http.com)
- [React Router Documentation](https://reactrouter.com)

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the backend logs
3. Check browser console for errors
4. Verify API connectivity

---

**Happy coding!** 🚀
