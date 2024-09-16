# Payloads :-

from faker import Faker
import json

faker = Faker()

def payload_create_booking():
    payload = {
        "firstname": "John",
        "lastname": "Nolan",
        "totalprice": 12345,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-12-23",
            "checkout": "2024-12-27"
        },
        "additionalneeds": "Dinner"
    }
    return payload

def payload_create_booking_dynamic():
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2024-12-23",
            "checkout": "2024-12-27"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "Wifi", "Extra Bed"))
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload