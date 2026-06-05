import sqlite3
from sqlalchemy import create_engine, func, and_
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
from config.settings import DATABASE_URL, DATABASE_PATH
from database.models import Base, User, Customer, Service, ServiceCategory, Appointment, Staff
from database.models import Invoice, Product, Transaction, VisitHistory, StaffAttendance
from utils.security import hash_password
import os
from datetime import datetime, date

class DatabaseManager:
    def __init__(self):
        os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
        self.engine = create_engine(
            DATABASE_URL,
            connect_args={'check_same_thread': False},
            poolclass=StaticPool
        )
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)
        self.init_database()
    
    def init_database(self):
        Base.metadata.create_all(bind=self.engine)
        self._init_default_data()
    
    def get_session(self) -> Session:
        return self.SessionLocal()
    
    def _init_default_data(self):
        session = self.get_session()
        try:
            admin_exists = session.query(User).filter_by(username='admin').first()
            if not admin_exists:
                admin_user = User(
                    username='admin',
                    password_hash=hash_password('admin123'),
                    email='admin@salon.com',
                    full_name='Administrator',
                    role='admin',
                    is_active=True
                )
                session.add(admin_user)
            
            categories_data = [
                ('Hair Services', 'Professional hair treatments'),
                ('Facial Services', 'Facial treatments'),
                ('Nail Services', 'Manicure and pedicure'),
                ('Makeup Services', 'Professional makeup'),
                ('Skin Services', 'Skin treatments'),
                ('Massage & Spa', 'Relaxation services')
            ]
            
            for cat_name, description in categories_data:
                cat_exists = session.query(ServiceCategory).filter_by(name=cat_name).first()
                if not cat_exists:
                    category = ServiceCategory(name=cat_name, description=description)
                    session.add(category)
            
            session.commit()
        except Exception as e:
            session.rollback()
        finally:
            session.close()
    
    def create_user(self, username: str, password: str, email: str = None, full_name: str = None, role: str = 'staff') -> User:
        session = self.get_session()
        try:
            if session.query(User).filter_by(username=username).first():
                raise ValueError(f"Username '{username}' already exists")
            user = User(username=username, password_hash=hash_password(password), email=email, full_name=full_name, role=role, is_active=True)
            session.add(user)
            session.commit()
            return user
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    def get_user_by_username(self, username: str) -> User:
        session = self.get_session()
        try:
            return session.query(User).filter_by(username=username).first()
        finally:
            session.close()
    
    def update_last_login(self, user_id: int):
        session = self.get_session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                user.last_login = datetime.now()
                session.commit()
        finally:
            session.close()
    
    def create_customer(self, name: str, phone: str, email: str = None, address: str = None, dob: date = None, notes: str = None) -> Customer:
        session = self.get_session()
        try:
            if session.query(Customer).filter_by(phone=phone).first():
                raise ValueError(f"Phone number '{phone}' already exists")
            customer = Customer(name=name, phone=phone, email=email, address=address, date_of_birth=dob, notes=notes)
            session.add(customer)
            session.commit()
            return customer
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    def get_customer(self, customer_id: int) -> Customer:
        session = self.get_session()
        try:
            return session.query(Customer).filter_by(id=customer_id).first()
        finally:
            session.close()
    
    def get_all_customers(self) -> list:
        session = self.get_session()
        try:
            return session.query(Customer).all()
        finally:
            session.close()
    
    def search_customers(self, search_term: str) -> list:
        session = self.get_session()
        try:
            search = f"%{search_term}%"
            return session.query(Customer).filter((Customer.name.ilike(search)) | (Customer.phone.ilike(search)) | (Customer.email.ilike(search))).all()
        finally:
            session.close()
    
    def update_customer(self, customer_id: int, **kwargs) -> Customer:
        session = self.get_session()
        try:
            customer = session.query(Customer).filter_by(id=customer_id).first()
            if not customer:
                raise ValueError(f"Customer with ID {customer_id} not found")
            for key, value in kwargs.items():
                if hasattr(customer, key):
                    setattr(customer, key, value)
            session.commit()
            return customer
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    def delete_customer(self, customer_id: int):
        session = self.get_session()
        try:
            customer = session.query(Customer).filter_by(id=customer_id).first()
            if customer:
                session.delete(customer)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    def create_service(self, name: str, category_id: int, price: float, duration: int, description: str = None) -> Service:
        session = self.get_session()
        try:
            service = Service(name=name, category_id=category_id, price=price, duration=duration, description=description)
            session.add(service)
            session.commit()
            return service
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    def get_all_services(self) -> list:
        session = self.get_session()
        try:
            return session.query(Service).filter_by(is_active=True).all()
        finally:
            session.close()
    
    def get_services_by_category(self, category_id: int) -> list:
        session = self.get_session()
        try:
            return session.query(Service).filter_by(category_id=category_id, is_active=True).all()
        finally:
            session.close()
    
    def get_all_categories(self) -> list:
        session = self.get_session()
        try:
            return session.query(ServiceCategory).all()
        finally:
            session.close()
    
    def create_appointment(self, customer_id: int, service_id: int, appointment_date: date, appointment_time, staff_id: int = None, notes: str = None) -> Appointment:
        session = self.get_session()
        try:
            appointment = Appointment(customer_id=customer_id, service_id=service_id, staff_id=staff_id, appointment_date=appointment_date, appointment_time=appointment_time, notes=notes)
            session.add(appointment)
            session.commit()
            return appointment
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    def get_today_appointments(self) -> list:
        session = self.get_session()
        try:
            return session.query(Appointment).filter(and_(Appointment.appointment_date == date.today(), Appointment.status != 'cancelled')).all()
        finally:
            session.close()
    
    def get_all_appointments(self) -> list:
        session = self.get_session()
        try:
            return session.query(Appointment).all()
        finally:
            session.close()
    
    def create_staff(self, name: str, phone: str, position: str, salary: float, hire_date: date, email: str = None, specialization: str = None) -> Staff:
        session = self.get_session()
        try:
            staff = Staff(name=name, phone=phone, email=email, position=position, salary=salary, hire_date=hire_date, specialization=specialization)
            session.add(staff)
            session.commit()
            return staff
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    def get_all_staff(self) -> list:
        session = self.get_session()
        try:
            return session.query(Staff).filter_by(is_active=True).all()
        finally:
            session.close()
    
    def create_invoice(self, customer_id: int, invoice_number: str, subtotal: float, gst_rate: float, discount_amount: float = 0.0, payment_method: str = None, appointment_id: int = None) -> Invoice:
        session = self.get_session()
        try:
            gst_amount = subtotal * (gst_rate / 100)
            total = subtotal + gst_amount - discount_amount
            invoice = Invoice(invoice_number=invoice_number, customer_id=customer_id, appointment_id=appointment_id, subtotal=subtotal, gst_amount=gst_amount, gst_rate=gst_rate, discount_amount=discount_amount, total_amount=total, payment_method=payment_method)
            session.add(invoice)
            session.commit()
            return invoice
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
    
    def get_today_revenue(self) -> float:
        session = self.get_session()
        try:
            today = date.today()
            result = session.query(func.sum(Invoice.total_amount)).filter(and_(func.date(Invoice.invoice_date) == today, Invoice.payment_status == 'completed')).scalar()
            return result or 0.0
        finally:
            session.close()
    
    def get_monthly_revenue(self) -> float:
        session = self.get_session()
        try:
            today = date.today()
            result = session.query(func.sum(Invoice.total_amount)).filter(and_(func.strftime('%Y-%m', Invoice.invoice_date) == today.strftime('%Y-%m'), Invoice.payment_status == 'completed')).scalar()
            return result or 0.0
        finally:
            session.close()
    
    def get_total_customers(self) -> int:
        session = self.get_session()
        try:
            return session.query(func.count(Customer.id)).scalar() or 0
        finally:
            session.close()
    
    def get_total_staff(self) -> int:
        session = self.get_session()
        try:
            return session.query(func.count(Staff.id)).filter_by(is_active=True).scalar() or 0
        finally:
            session.close()
    
    def get_total_services(self) -> int:
        session = self.get_session()
        try:
            return session.query(func.count(Service.id)).filter_by(is_active=True).scalar() or 0
        finally:
            session.close()
    
    def get_today_appointments_count(self) -> int:
        session = self.get_session()
        try:
            return session.query(func.count(Appointment.id)).filter(and_(Appointment.appointment_date == date.today(), Appointment.status != 'cancelled')).scalar() or 0
        finally:
            session.close()
