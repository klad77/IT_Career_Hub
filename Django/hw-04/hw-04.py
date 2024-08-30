from sqlalchemy import create_engine, Column, Integer, String, Boolean, Numeric, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///example.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)


# Добавление категорий
def insert_categories(session):
    categories = [
        Category(name="Электроника", description="Гаджеты и устройства."),
        Category(name="Книги", description="Печатные книги и электронные книги."),
        Category(name="Одежда", description="Одежда для мужчин и женщин.")
    ]
    session.add_all(categories)
    session.commit()
    return categories


# Добавление продуктов
def insert_products(session):
    categories = session.query(Category).all()
    products = [
        Product(name="Смартфон", price=299.99, in_stock=True, category=categories[0]),
        Product(name="Ноутбук", price=499.99, in_stock=True, category=categories[0]),
        Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category=categories[1]),
        Product(name="Джинсы", price=40.50, in_stock=False, category=categories[2]),
        Product(name="Футболка", price=20.00, in_stock=True, category=categories[2]),
    ]
    session.add_all(products)
    session.commit()


# все записи из таблицы categories
def get_all_categories(session):
    categories = session.query(Category).all()
    for category in categories:
        print(category.name, category.description)


# Для категории выведите все связанные с ней продукты, включая их названия и цены.
def get_product_by_categories(session):
    categories = session.query(Category).all()
    for category in categories:
        print(f'Категория: {category.name}')
        for product in category.products:
            print(f' - {product.name}: {product.price}')


# Обновление данных
def change_price_of_product(session):
    product = session.query(Product).filter_by(name='Смартфон').first()
    if product:
        product.price = 349.99
    session.commit()


def count_products_per_category(session):
    results = session.query(
        Category.name,  # Имя категории
        func.count(Product.id)  # Количество продуктов в этой категории
    ).join(Product).group_by(Category.id).all()  # Группируем по ID категории

    # Выводим результаты
    for category_name, product_count in results:
        print(f"Категория: {category_name}, Количество продуктов: {product_count}")


def filter_categories_with_multiple_products(session):
    # Выполняем запрос для поиска категорий с более чем одним продуктом
    results = session.query(
        Category.name,  # Имя категории
        func.count(Product.id)  # Количество продуктов в категории
    ).join(Product).group_by(Category.id).having(func.count(Product.id) > 1).all()  # Группируем и фильтруем

    # Выводим результаты
    for category_name, product_count in results:
        print(f"Категория: {category_name}, Количество продуктов: {product_count}")

# insert_categories(session)
# insert_products(session)
# get_all_categories(session)  # все записи из таблицы categories
# get_product_by_categories(session)
# change_price_of_product(session)
# count_products_per_category(session)
filter_categories_with_multiple_products(session)
