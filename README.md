# Backend Setup Guide

Follow these steps to activate and run the backend application.

## Prerequisites

- Python 3.x installed
- MySQL server installed and running

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Database

Create a MySQL database named `orders_db`:

```bash
mysql -u root -p -e "CREATE DATABASE orders_db;"
```

### 5. Configure Environment Variables

Create a `.env` file in the backend directory and fill in the following database configuration:

```
# Database Configuration
DB_USER = 
DB_PASSWORD = 
DB_HOST = 
DB_PORT = 
DB_NAME = 
```

**Example:**
```
# Database Configuration
DB_USER = root
DB_PASSWORD = your_password
DB_HOST = localhost
DB_PORT = 3306
DB_NAME = orders_db
```

### 6. Run the Application

```bash
python app.py
```

The backend application should now be running!
