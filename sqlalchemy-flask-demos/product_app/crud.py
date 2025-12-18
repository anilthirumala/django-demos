from models import Product
from database import SessionLocal

def get_all_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products

def create_product(name, price, description):
    db = SessionLocal()
    product = Product(name=name, price=price, description=description)
    db.add(product)
    db.commit()
    db.refresh(product)
    db.close()
    return product

def get_product(id):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == id).first()
    db.close()
    return product

def update_product(id, name, price, description):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == id).first()
    product.name = name
    product.price = price
    product.description = description
    db.commit()
    db.close()

def delete_product(id):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == id).first()
    db.delete(product)
    db.commit()
    db.close()