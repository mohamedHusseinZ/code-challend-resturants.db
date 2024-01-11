#!/usr/bin/env python3

from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    restaurant1 = session.query(Restaurant).first()

    # return details of all the restaurant instance reviews
    print('\n all_reviews() ')
    print(restaurant1.all_reviews())

    # return all the restaurant instance reviews
    print('\n restaurant_reviews ')
    print(restaurant1.restaurant_reviews)

    # return all the customers who have reviewed this restaurant
    print('\n restaurant_customers ')
    print(restaurant1.restaurant_customers)

    print('\n fanciest_restaurant() ')
    # returns the fanciest(most-expensive) restaurant of all the restaurants
    print(Restaurant.fanciest_restaurant())

    customer1 = session.query(Customer).first()

    print('\n customer_reviews ')
    # returns the customer reviews
    print(customer1.customer_reviews)

    print('\n customer_restaurants ')
    # to return the customer reviews
    print(customer1.customer_restaurants)

    print('\n full_name -')
    # to return customer full_name
    print(customer1.full_name)

    print('\n favorite_restaurant ')
    # to return restaurant with the highest review for this customer
    print(customer1.favorite_restaurant())

    print('\n add_review() ')
    # to add a review and return it
    new_review = customer1.add_review(restaurant1, 8, "Honey, I'm so high!")
    print(f"Added Review: {new_review}")

    print('\n delete_reviews() ')
    # to delete reviews that belong to specific restaurants
    customer1.delete_reviews(restaurant1)

    review1 = session.query(Review).first()
    print('\n review_customer -------')
    # return customer
    print(review1.review_customer)

    print('\n review_restaurant -------')
    # return customer
    print(review1.review_restaurant)

    print('\n full_review() ')
    # return full review details
    print(review1.full_review())
