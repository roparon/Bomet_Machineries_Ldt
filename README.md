# Bomet Machineries Ltd – Ecommerce Website  

An ecommerce platform for **agricultural machinery and spare parts**, built with **Flask, Python, HTML, CSS, and SQLAlchemy**.  
This project provides a simple but scalable foundation for selling products online, with both **customer-facing pages** and an **admin dashboard**.  

---

## Features  

- User Authentication – Register, login, and logout with secure password hashing  
- Product Catalog – Browse machinery and spare parts with descriptions and prices  
- Orders & Checkout – Customers can place orders and track them  
- Admin Dashboard – Add, update, and manage products and stock  
- Database Integration – SQLAlchemy ORM for handling models and persistence  
- Frontend Templates – HTML & CSS with room for Bootstrap or Tailwind  

---

## Tech Stack  

- **Backend**: Flask (Python)  
- **Frontend**: HTML, CSS (Bootstrap or custom)  
- **Database**: SQLite (default), can be upgraded to MySQL/PostgreSQL  
- **Authentication**: Flask-Login  
- **ORM**: SQLAlchemy  
- **Deployment**: Localhost (dev), production-ready with WSGI server (Gunicorn/NGINX)  

---

## Project Structure  

Bomet_Machineries_Ldt/
│── app/
│ ├── routes/ # Blueprints (auth, shop, admin)
│ │ ├── auth.py
│ │ ├── shop_routes.py
│ │ └── admin_routes.py
│ ├── templates/ # Jinja2 templates (HTML files)
│ ├── static/ # CSS, JS, images
│ ├── models.py # SQLAlchemy models
│ ├── extensions.py # Database, login_manager setup
│ └── init.py # App factory
│
│── config.py # Configuration settings
│── run.py # Entry point to run Flask app
│── requirements.txt # Dependencies
│── README.md # Project documentation

yaml
Copy code

---

## Getting Started  

### 1. Clone the repository  
```bash
git clone https://github.com/yourusername/Bomet_Machineries_Ldt.git
cd Bomet_Machineries_Ldt
2. Create a virtual environment and activate it
bash
Copy code
python3 -m venv .machine
source .machine/bin/activate   # On Linux/Mac
.machine\Scripts\activate      # On Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the application
bash
Copy code
python run.py
5. Open in your browser
cpp
Copy code
http://127.0.0.1:5000
Database Models (Core)
User – customer & admin accounts

Product – machinery & spare parts listings

Order – customer orders

OrderItem – products within an order

Future models can include Category, Cart, Payment, Reviews, and ShippingAddress.

Roadmap / Future Enhancements
Product Categories & Filtering

Mpesa / Card Payment Integration

Customer Reviews & Ratings

Shipping & Delivery Tracking

Inventory Management (stock in/out logs)

Contributing
Contributions are welcome!

Fork the repo

Create a new branch (git checkout -b feature/new-feature)

Commit changes (git commit -m "Added new feature")

Push to your branch (git push origin feature/new-feature)

Open a Pull Request

License
This project is licensed under the MIT License – see the LICENSE file for details.

Author
Bomet Machineries Ltd Project
Developed by Aron Arap Rop