from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from database import Base, engine, get_db



class Product(Base):
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum("finished", "semi-finished", "raw"), nullable=False)
    description = Column(String(250))
    product_image = Column(String(500))  
    sku = Column(String(100), unique=True, nullable=False)
    unit_of_measure = Column(Enum("mtr", "mm", "ltr", "ml", "cm", "mg", "gm", "unit", "pack"), nullable=False)
    lead_time = Column(Integer, nullable=False)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    updated_date = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    __tablename__ = "products"

Base.metadata.create_all(bind=engine)
    
class ProductCreate(BaseModel):
    name: str
    category: str
    description: str
    product_image: str
    sku: str
    unit_of_measure: str
    lead_time: int

class ProductUpdate(BaseModel):
    name: str = None
    category: str = None
    description: str = None
    product_image: str = None
    sku: str = None
    unit_of_measure: str = None
    lead_time: int = None

app = FastAPI()

@app.get("/product/list")
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Product).offset(skip).limit(limit).all()

@app.get("/product/{pid}/info")
def get_product(pid: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/add")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"message": "Product added successfully", "product": db_product}

@app.put("/product/{pid}/update")
def update_product(pid: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == pid).first()
    if not db_product:
        raise HTTPException(status_code=404, detail=f"Product with ID {pid} not found")

    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return {"message": "Product updated successfully", "product": db_product}

