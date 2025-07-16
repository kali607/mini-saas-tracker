# 🛠️ Mini SaaS — Issues & Insights Tracker

A full-stack mini SaaS platform to track issues, monitor stats, and gain insights with Google OAuth login, charts, filters, and more.

---

## 🚀 Tech Stack

### 🔧 Backend
- **Django** + **Django REST Framework**
- **PostgreSQL** (via Docker)
- **dj-rest-auth** + **allauth** for authentication
- **Google OAuth 2.0** login integration
- **Celery** + **Redis** (for future task queues)
- **Docker** support for easy development

### 🎨 Frontend
- **SvelteKit**
- **Tailwind CSS**
- **Chart.js** for data visualization

### 📦 DevOps
- **Docker Compose** setup
- **GitHub Actions** (CI/CD setup coming)
- `.env` file for environment variables

---

## 🔐 Features

- User authentication (with Google OAuth 2.0)
- Secure backend + protected API endpoints
- Issue creation, listing, filtering
- Chart dashboard for issue stats (by severity, user, date)
- Fully containerized using Docker
- Environment separation for dev & prod

---

## 🧪 Project Structure

