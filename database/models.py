from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, ForeignKey, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(120), unique=True)
    full_name = Column(String(150))
    role = Column(String(50), default='staff')
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    last_login = Column(DateTime)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, index=True)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True)
    address = Column(Text)
    date_of_birth = Column(Date)
    registration_date = Column(DateTime, default=datetime.now)
    last_visit_date = Column(DateTime)
    notes = Column(Text)
    loyalty_points = Column(Integer, default=0)
    total_spent = Column(Float, default=0.0)

class ServiceCategory(Base):
    __tablename__ = 'service_categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text)

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, index=True)
    category_id = Column(Integer, ForeignKey('service_categories.id'), nullable=False)
    price = Column(Float, nullable=False)
    duration = Column(Integer)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    appointment_date = Column(Date, nullable=False, index=True)
    appointment_time = Column(Time, nullable=False)
    status = Column(String(50), default='scheduled')
    notes = Column(Text)
    reminder_sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, index=True)
    phone = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True)
    position = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)
    hire_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)
    specialization = Column(Text)
    performance_rating = Column(Float, default=0.0)
    total_commission = Column(Float, default=0.0)

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    invoice_number = Column(String(50), unique=True, nullable=False, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    appointment_id = Column(Integer, ForeignKey('appointments.id'))
    invoice_date = Column(DateTime, default=datetime.now, index=True)
    subtotal = Column(Float, default=0.0)
    gst_amount = Column(Float, default=0.0)
    gst_rate = Column(Float, default=18.0)
    discount_amount = Column(Float, default=0.0)
    total_amount = Column(Float, nullable=False)
    payment_method = Column(String(50))
    payment_status = Column(String(50), default='pending')
    notes = Column(Text)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False, index=True)
    category = Column(String(100), nullable=False)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, nullable=False)
    supplier = Column(String(150))
    expiry_date = Column(Date)
    stock_alert_quantity = Column(Integer, default=5)
    added_date = Column(DateTime, default=datetime.now)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    amount = Column(Float, nullable=False)
    transaction_type = Column(String(50))
    payment_method = Column(String(50))
    reference_number = Column(String(100))
    description = Column(Text)
    transaction_date = Column(DateTime, default=datetime.now, index=True)

class VisitHistory(Base):
    __tablename__ = 'visit_history'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    visit_date = Column(DateTime, default=datetime.now, index=True)
    service_id = Column(Integer, ForeignKey('services.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))
    amount_spent = Column(Float)
    notes = Column(Text)

class StaffAttendance(Base):
    __tablename__ = 'staff_attendance'
    id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, ForeignKey('staff.id'), nullable=False)
    date = Column(Date, nullable=False, index=True)
    check_in_time = Column(Time)
    check_out_time = Column(Time)
    status = Column(String(50))
    notes = Column(Text)
