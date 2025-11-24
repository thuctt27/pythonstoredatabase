from sqlalchemy import select
from models import Category, Product, Customer, Base
from database import engine, Session
import sys
import csv 

def create_table():
    Base.metadata.create_all(engine)

def drop_table():
    Base.metadata.drop_all(engine)

def import_table(csv_path="products.csv"):
    session = Session()
    with open(csv_path,newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            category = row['category']
            possible_category = session.execute(select(Category).where(Category.name == category)).scalar()

            if not possible_category:
                category_obj = Category(name=category)
                session.add(category_obj)
            else:
                category_obj = possible_category

            prod = Product(
                name = row['name'],
                price = float(row['price']),
                available = int(row['available']),
                category=category_obj
            )
            session.add(prod)
    session.commit()

def import_customers(csv_path="customers.csv"):
    session = Session()
    with open(csv_path,newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cus = Customer(
                name = row['name'],
                phone = row['phone']
            )
            session.add(cus)
        session.commit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('please run script with either create,drop,or import')
    else:
        command = sys.argv[1].lower()
        if command == "create":
            create_table()
        elif command == "drop":
            drop_table()
        elif command == "import":
            import_table()
        elif command == "customers":
            import_customers()
        else:
            print("invalid argument, please run script with either create,drop,or import")
    
