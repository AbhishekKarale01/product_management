# FastAPI Product Management

This project is a **FastAPI-based RESTful API** for managing products using **MySQL** as the backend database. It includes CRUD operations to **list, retrieve, add, and update** products.

## Features
-  List all products with **pagination**
-  Retrieve **product details** by ID
-  Add a **new product**
-  Update an **existing product**
-  Uses **FastAPI, SQLAlchemy, Pydantic**
-  MySQL as the **database backend**
-  Supports API documentation using **Swagger UI**

---

## Requirements
- **Python 3.11+**
- **FastAPI**
- **Pydantic** (for data validation)
- **SQLAlchemy** (ORM)
- **MySQL Database**
- **MySQL Connector** (`mysql-connector-python`)

---

## Installation & Setup

It is recommended to create a virtual environment before installing dependencies to keep the project isolated.  

### For Windows  
python -m venv venv
venv\Scripts\activate

### For Mac/Linux
python3 -m venv venv
source venv/bin/activate

###  Install Dependencies
pip install -r requirements.txt
