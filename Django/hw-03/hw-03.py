from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Создание движка SQLite в памяти
engine = create_engine('sqlite:///:memory:')

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Базовый класс для моделей
Base = declarative_base()


# Модель категории
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    products = relationship("Product", back_populates="category")


# Модель продукта
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")


# Создание таблиц в базе данных
Base.metadata.create_all(engine)
