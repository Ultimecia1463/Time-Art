# ⌚ Time-Art — Luxury Watch Store

Time-Art is a full-stack e-commerce web application for selling luxury watches.  
It is built with **Django**, styled using **Tailwind CSS + DaisyUI (no Node.js)**, and uses **PostgreSQL (Supabase)** as the database.

The application supports user authentication, product browsing, cart management, order placement, and order history.

---

## ✨ Features

- User authentication (login / register)
- Product listing with detailed product pages
- Shopping cart functionality
- Order placement & order history
- Clean, responsive UI using DaisyUI
- Secure configuration using environment variables
- PostgreSQL database hosted on Supabase

---

## 🛠 Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- PostgreSQL (Supabase)
- python-dotenv

### Frontend
- Tailwind CSS v4 (Standalone CLI)
- DaisyUI v5
- No Node.js or npm required

---

## 📁 Project Structure (Simplified)

```
Time-Art/
├── config/              # Django project settings
├── store/               # Main app (models, views, templates)
│   ├── static/css/      # Tailwind & DaisyUI output
│   └── templates/       # HTML templates
├── .env                 # Environment variables (not committed)
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Time-Art.git
cd Time-Art
```

---

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Linux / macOS
```

---

### 3️⃣ Install backend dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure environment variables

Create a `.env` file at the project root:

```env
SECRET_KEY=your-secret-key
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=your-supabase-host
DB_PORT=5432
```

> ⚠️ `.env` is ignored via `.gitignore` and should never be committed.

---

## 🎨 Tailwind CSS + DaisyUI Setup (No Node.js)

This project uses **Tailwind CSS standalone binary** with **DaisyUI**, so Node.js is not required.

### Install Tailwind & DaisyUI (Windows)

```bash
cd store/static/css
powershell -c "irm daisyui.com/fast.ps1 | iex"
```

This command:
- Downloads Tailwind CSS standalone binary
- Downloads DaisyUI plugin
- Creates `input.css`
- Generates `output.css`

---

### Run Tailwind watcher (development)

```bash
cd store/static/css
.\tailwindcss.exe -i input.css -o output.css --watch
```

👉 Leave this running while developing.

To generate CSS once (for production):

```bash
.\tailwindcss.exe -i input.css -o output.css
```

---

## ▶️ Run the Django Server

In a **new terminal**, from project root:

```bash
python manage.py migrate
python manage.py runserver
```

Open:
```
http://127.0.0.1:8000/
```

---

## 🔐 Security Notes

- Secrets are managed using **python-dotenv**
- Database credentials are not hardcoded
- Ready for production environment variable setup

---

## 📌 Future Improvements

- Payment gateway integration (Razorpay / Stripe)
- Product reviews & ratings
- Wishlist functionality
- Admin analytics dashboard
- API documentation (Swagger)

---

## 👤 Author

**Ansh Sharma**  
Full-Stack Developer

Built as a hands-on project to practice Django, modern UI tooling, and clean architecture.
