# E-Commerce Site

A fully functional e-commerce website built with Django, providing a seamless shopping experience for users with a powerful admin dashboard for managing products and orders.

## 📋 Overview

This project is a complete and functional online shop application built using the Django framework. It allows users to browse products, add them to their shopping cart, and complete purchases easily. It also provides an administrative dashboard for managing products, orders, and users.

## ✨ Key Features

- **Product Display**: Attractive interface for displaying products with images, prices, and details
- **Shopping Cart**: Easy addition and management of products in the cart
- **User System**: Login, registration, and account management
- **Admin Dashboard**: Django Admin interface for complete store management
- **Order Management**: Track orders and their statuses
- **Responsive Design**: Works on all devices (desktop, tablet, mobile)
- **Search & Filter**: Ability to search for products and filter by categories

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (optional but recommended)
- Git

## 📥 Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/mousa149/E-Commerce-site.git
cd E-Commerce-site
```

### Step 2: Create a Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Required Packages
```bash
pip install django
pip install pillow  # For image processing
# Add any other required packages
```

### Step 4: Set Up the Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser
```bash
python manage.py createsuperuser
```

Enter the username, email, and password when prompted.

### Step 6: Run the Server
```bash
python manage.py runserver
```

Now you can visit the site at: `http://127.0.0.1:8000/`

Admin panel is available at: `http://127.0.0.1:8000/admin/`

## 🚀 Usage

### For Regular Users

1. **Register**: Create a new account from the registration page
2. **Browse Products**: View available products on the homepage
3. **Add to Cart**: Click the "Add to Cart" button for desired products
4. **Complete Order**: Go to the shopping cart and complete the purchase

### For Administrators

1. **Admin Login**: Use the superuser account to access `/admin/`
2. **Manage Products**: Add, edit, or delete products
3. **Manage Orders**: Track and update order statuses
4. **Manage Users**: Monitor user accounts and permissions

## 📁 Project Structure
```
E-Commerce-site/
├── ecomsite/           # Main project settings
│   ├── settings.py     # Django settings
│   ├── urls.py         # Main URL routing
│   └── wsgi.py         # WSGI interface
├── shop/               # Main shop application
│   ├── models.py       # Database models
│   ├── views.py        # Views
│   ├── urls.py         # App URLs
│   ├── templates/      # HTML templates
│   └── static/         # CSS and JavaScript files
├── db.sqlite3          # SQLite database
├── manage.py           # Django management tool
└── .gitignore          # Files ignored by Git
```

## ⚙️ Additional Configuration

### Configure Static Files
```bash
python manage.py collectstatic
```

### Configure Media Files

Ensure you have a `media/` folder in your project to store uploaded product images.

### Database Settings

The project uses SQLite by default. To use another database like PostgreSQL or MySQL, modify the `DATABASES` settings in `settings.py`.

## 🧪 Testing

To run tests:
```bash
python manage.py test
```

## 🚀 Deployment

### Preparing for Deployment

1. Update `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

2. Collect static files:
```bash
python manage.py collectstatic
```

3. Use a production server like Gunicorn:
```bash
pip install gunicorn
gunicorn ecomsite.wsgi:application
```

### Recommended Deployment Platforms

- **Heroku**: Easy to use and free to start
- **PythonAnywhere**: Specialized for Python applications
- **DigitalOcean**: Customizable servers
- **AWS**: For large-scale projects

## 🤝 Contributing

We welcome your contributions! To contribute to this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Test thoroughly
5. Commit changes (`git commit -m 'Add new feature'`)
6. Push to branch (`git push origin feature/new-feature`)
7. Open a Pull Request

## 🐛 Troubleshooting

If you encounter any issues:

1. Ensure all requirements are installed correctly
2. Verify the database has been migrated
3. Check error messages in the terminal
4. If issues persist, open a new Issue on GitHub

## 📚 Resources and References

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Python Documentation](https://docs.python.org/3/)

## 🔐 Security

- Don't share your `settings.py` file containing `SECRET_KEY`
- Use environment variables for sensitive data
- Always update Django to the latest secure version
- Use HTTPS in production environment

## 📜 License

This project is open source and available for personal and educational use.

## 👤 Developer

**mousa149**
- GitHub: [@mousa149](https://github.com/mousa149)

## 🙏 Acknowledgments

Special thanks to the Django community for excellent documentation and continuous support.

## 📞 Contact

If you have any questions or suggestions:
- Open an Issue on GitHub
- Contact through the project page

## 🌟 Future Enhancements

- [ ] Payment gateway integration
- [ ] Email notifications for orders
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Advanced search filters
- [ ] Multi-language support
- [ ] API for mobile apps

## 📊 Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (can be configured for PostgreSQL, MySQL)
- **Admin Interface**: Django Admin

---

Made with ❤️ using Django
