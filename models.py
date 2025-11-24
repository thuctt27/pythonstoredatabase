from sqlalchemy import String, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from database import Base

class Product(Base):
    __tablename__ = "product"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    price= mapped_column(DECIMAL(10,2))
    available = mapped_column(Integer, default=0)
    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")


    def __str__(self):
        return f"id:{self.id},name: {self.name},price:{self.price},inventory:{self.available},category:{self.category}"

class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    products = relationship("Product", back_populates="category")

    
class Customer(Base):
    __tablename__ = 'customer'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    phone = mapped_column(String)

    def __str__(self):
        return f"{self.name} {self.phone}"

