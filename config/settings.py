"""Application Configuration and Settings"""

import os
from pathlib import Path

# Application Information
APP_NAME = "Salon Management System"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Salon Management Team"

# Database Settings
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = os.path.join(BASE_DIR, "database", "salon_management.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Ensure database directory exists
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

# UI Theme Settings
THEME_PRIMARY_COLOR = "#001f3f"  # Navy Blue
THEME_SECONDARY_COLOR = "#ffffff"  # White
THEME_ACCENT_COLOR = "#0074D9"  # Bright Blue
THEME_SUCCESS_COLOR = "#2ECC40"  # Green
THEME_DANGER_COLOR = "#FF4136"  # Red
THEME_WARNING_COLOR = "#FF851B"  # Orange

# Font Settings
FONT_FAMILY = "Segoe UI"
FONT_SIZE_SMALL = 10
FONT_SIZE_NORMAL = 11
FONT_SIZE_LARGE = 12
FONT_SIZE_TITLE = 16
FONT_SIZE_HEADING = 14

# Animation Settings
ANIMATION_DURATION = 300  # milliseconds

# Security Settings
PASSWORD_MIN_LENGTH = 6
MAX_LOGIN_ATTEMPTS = 5
SESSION_TIMEOUT = 3600  # 1 hour in seconds

# Default Admin Credentials (change in production)
DEFAULT_ADMIN_USERNAME = "admin"
DEFAULT_ADMIN_PASSWORD = "admin123"

# GST Settings
DEFAULT_GST_RATE = 18  # Percentage

# Window Settings
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
WINDOW_MIN_WIDTH = 1200
WINDOW_MIN_HEIGHT = 700

# Application Paths
ICON_PATH = os.path.join(BASE_DIR, "assets", "icons")
STYLE_PATH = os.path.join(BASE_DIR, "assets", "styles")
