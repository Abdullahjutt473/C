# Salon Management System

A comprehensive, professional desktop application for managing salon operations built with PyQt6 and SQLite.

## Features

- **User Authentication**: Secure login and signup system with password hashing
- **Dashboard**: Real-time statistics and business metrics
- **Customer Management**: Complete customer database with history and loyalty points
- **Appointment Management**: Book, reschedule, and manage appointments
- **Services Management**: Organize services by categories with pricing
- **Billing & Invoicing**: Generate professional invoices with PDF export
- **Sales & Reports**: Comprehensive reporting with charts and graphs
- **Staff Management**: Track staff, attendance, salary, and performance
- **Inventory Management**: Manage products and stock alerts
- **Settings**: Backup, restore, and customize application

## Requirements

- Python 3.8+
- PyQt6
- SQLite3

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

On first run, the database will be automatically created with all necessary tables.

## Project Structure

```
salon_management/
├── main.py                    # Application entry point
├── requirements.txt          # Python dependencies
├── database/
│   ├── db_manager.py        # Database operations
│   ├── models.py            # Database models and schema
│   └── init_db.py           # Database initialization
├── ui/
│   ├── main_window.py       # Main application window
│   ├── login_window.py      # Login/Signup interface
│   ├── dashboard.py         # Dashboard view
│   ├── customers.py         # Customer management
│   ├── appointments.py      # Appointment management
│   ├── services.py          # Services management
│   ├── billing.py           # Billing and invoices
│   ├── sales.py             # Sales reports
│   ├── staff.py             # Staff management
│   ├── inventory.py         # Inventory management
│   ├── reports.py           # Reports generation
│   └── settings.py          # Application settings
├── utils/
│   ├── helpers.py           # Utility functions
│   ├── validators.py        # Input validation
│   ├── security.py          # Security functions
│   └── pdf_generator.py     # PDF generation
├── assets/
│   ├── styles.qss           # PyQt6 stylesheets
│   └── icons/               # Application icons
└── config/
    └── settings.py          # Configuration
```

## Default Login

Username: `admin`
Password: `admin123`

## License

Proprietary - All rights reserved
