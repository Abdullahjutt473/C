from datetime import datetime, date
import re

APP_NAME = "Salon Management System"
APP_VERSION = "1.0.0"

def format_currency(amount: float) -> str:
    return f"INR {amount:,.2f}"

def format_datetime(dt: datetime) -> str:
    if dt is None:
        return "-"
    return dt.strftime("%d-%m-%Y %H:%M")

def format_date(d: date) -> str:
    if d is None:
        return "-"
    return d.strftime("%d-%m-%Y")

def format_time(t) -> str:
    if t is None:
        return "-"
    if isinstance(t, str):
        return t
    return t.strftime("%H:%M")

def get_initials(name: str) -> str:
    parts = name.split()
    return ''.join([p[0].upper() for p in parts if p])[:2]

def truncate_text(text: str, length: int = 50) -> str:
    if not text:
        return "-"
    if len(text) > length:
        return text[:length] + "..."
    return text

def generate_invoice_number() -> str:
    now = datetime.now()
    return f"INV-{now.strftime('%Y%m%d')}-{int(now.timestamp())}"

def format_phone(phone: str) -> str:
    digits = re.sub(r'\D', '', phone)
    if len(digits) >= 10:
        return f"+91-{digits[-10:-7]}-{digits[-7:-4]}-{digits[-4:]}"
    return phone

def calculate_age(dob: date) -> int:
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

def get_app_info() -> str:
    return f"{APP_NAME} v{APP_VERSION}"
