# Exercise 7: Faker Module

from faker import Faker

users = []

def add_users(num_users):
    fake = Faker()
    for _ in range(num_users):
        user = {
            'name' : fake.name(),
            'address' : fake.address(),
            'language_code' : fake.language_code()
        }
        users.append(user)

add_users(5)
for user in users:
    print(user)