# 🛍️ Vintage - Flask Fashion E-Commerce Website

Vintage is a responsive, user-friendly e-commerce web application built using **Flask** and **MySQL**, designed for showcasing fashion products. Users can register, log in, browse products, add items to their cart, and admins can manage the inventory through a dashboard.

---

## 🔧 Tech Stack

- 🐍 Python (Flask Framework)
- 🗃️ MySQL (Relational Database)
- 🌐 HTML5, CSS3, JavaScript (Frontend)
- 🖼️ Bootstrap (Styling and UI)
- 📦 Jinja2 Templating (Dynamic Pages)

---

## 📁 Folder Structure

vintage/
├── static/
│ └── images/ # Product and asset images
├── templates/
│ ├── homepage.html
│ ├── loginpage.html
│ ├── registerpage.html
│ ├── dashboard.html
│ ├── products.html
│ └── cart.html
└── app.py # Main Flask application


---

## ✅ Features

### 🧑‍💼 User
- Register & Login
- View all products
- Add products to cart
- View cart summary with total price
- Delete items from cart

### 🛠️ Admin
- Add, update, delete products
- Admin dashboard access (`email: murugan`, `password: murugan`)

---

## 📦 Database Schema

### `user_details`
- `id` (INT, PK)
- `name` (VARCHAR)
- `email` (VARCHAR)
- `password` (VARCHAR)

### `products`
- `product_code` (INT, PK)
- `product_name` (VARCHAR)
- `product_price` (FLOAT)
- `product_image` (VARCHAR)

### `user_cart`
- `product_code` (INT)
- `product_name` (VARCHAR)
- `product_price` (FLOAT)
- `product_image` (VARCHAR)
- `product_quantity` (INT)

---

## 🚀 How to Run Locally

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/vintage-flask.git
cd vintage-flask
```

<pre>Set up a virtual environment (optional but recommended)</pre>

![]
