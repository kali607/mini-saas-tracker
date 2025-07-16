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

```
mini-saas-tracker/
├── backend/
│   ├── users/         → Google OAuth + user logic
│   ├── issues/        → CRUD for issues
│   ├── stats/         → Stats & chart APIs
│   └── dashboard/     → Dashboard logic
├── frontend/
│   └── src/routes/    → SvelteKit pages
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Getting Started (Development)

### 🔑 Prerequisites

- Docker & Docker Compose
- Google OAuth credentials (Client ID & Secret)
- `.env` files (not committed)

### 📦 Run with Docker

```bash
# Build and run all containers
docker-compose up --build
```

Visit the frontend at:  
➡️ `http://localhost:5173`  
Backend API root:  
➡️ `http://localhost:8000/api/`

---

## 🔑 Environment Variables

Create a `.env` file inside the `backend/` folder:

```env
DEBUG=True
SECRET_KEY=your-django-secret

# PostgreSQL
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Django Environ Shortcut
DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
```

⚠️ **Never commit `.env` files. Add them to `.gitignore`.**

---

## 📈 Charts & Insights

- View charts filtered by **date**, **user**, and **severity**
- Uses `Chart.js` on frontend
- API data served by `/api/stats/severity/` on backend

---

## ✅ To-Do / Roadmap

- [x] Google OAuth Login
- [x] Severity chart with filters
- [ ] GitHub Actions CI/CD (next step)
- [ ] Unit tests (API + SvelteKit)
- [ ] Add Celery for background jobs (email/reporting)

---

## 🤝 Contributing

Pull requests are welcome. Open an issue first to discuss major changes.

---

## 📄 License

MIT License — Free to use and modify.

---

## 👨‍💻 Author

**Kasani Kali Krishna Mohan**  
[GitHub](https://github.com/kali607)

---
