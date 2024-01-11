from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

def seed_database():
    engine = create_engine('sqlite:///restaurants.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    customers = []
    for _ in range(10):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        session.commit()
        customers.append(customer)

    restaurants = []
    for _ in range(10):
        restaurant = Restaurant(
            name=fake.unique.name(),
            price=random.randint(4000, 10000)
        )
        session.add(restaurant)
        session.commit()
        restaurants.append(restaurant)

    reviews = []
    for restaurant in restaurants:
        for _ in range(random.randint(1, 10)):
            customer = random.choice(customers)
            review = Review(
                restaurant_id=restaurant.id,
                description=fake.sentence(),
                star_rating=random.randint(1, 10),
                customer_id=customer.id
            )
            if restaurant not in customer.restaurants:
                customer.reviews.append(review)
                session.commit()

    session.close()

if __name__ == '__main__':
    seed_database()

