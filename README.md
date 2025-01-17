
# EcoMart
EcoMart is a modern and scalable e-commerce platform built with Django. It provides a seamless shopping experience with features like product browsing, user authentication, secure payment processing, and order management.

### 🚀 Features
* User Authentication: Sign up, login, and profile management.
* Product Management: Add, edit, and delete products with images, descriptions, and pricing.
* Advanced Product Filtering: Search and filter products by category, price range, and more.
* Shopping Cart: Add products to the cart and manage quantities.
* Order Management: Track placed orders with detailed history.
* Payment Integration: Secure and reliable payment gateway.
* Responsive Design: Fully optimized for desktop and mobile devices.

### 🛠️ Technologies Used
* Django: A high-level Python web framework.
* SQLite: A lightweight database for development.
* Bootstrap: Front-end framework for styling.
* JavaScript: For dynamic web content (e.g., currency converter).
* Python 3.9: The programming language used for the project.

📂 Project Structure
```bash
EcoMart/
├── EcoMartApp/         # Project configuration
├── accounts/           # User authentication and profiles
├── media/              # Static files (CSS, JS, images)
├── products/           # Product app (models, views, templates)
├── manage.py           # Django management script
├── db.sqlite3          # Django database
└── requirements.txt    # Requirements file
```

## Installation

1. Clone the repository:

```bash
https://github.com/Onkar2104/EcoMart.git
```
2. Navigate to the project folder:

```bash
cd EcoMart
```

3. Set up a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Apply migrations:
```bash
python manage.py migrate
```
6. Create a superuser to access the admin panel:
```bash
python manage.py createsuperuser
```
7. Run the development server:
```bash
python manage.py runserver
```
8. Access the app in your browser at:
```bash
http://127.0.0.1:8000
```
## Live Demo

[EcoMart](http://65.0.170.109/)

Visit the site.


## 🤝 Contributing
We welcome contributions to EcoMart! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: git checkout -b feature-name.
3. Commit your changes: git commit -m "Add feature description".
4. Push to the branch: git push origin feature-name.
5. Submit a pull request.



## 🌟 Logo
![Logo](home/static/photos/logo3.png)


## 📷 Screenshots

![App Screenshot](home/static/photos/Screenshot1.png)
![Library Screenshot](home/static/photos/Screenshot12.png)

## 📬 Contact
For questions, feedback, or suggestions, feel free to reach out:

Author: Onkar Umakant Ijare
Email: ijareonkar2184@gmaill.com
GitHub: github.com/Onkar2104
LinkedIn: https://www.linkedin.com/in/onkarijare/
