from base64 import b64encode
from faker import Faker
import random


class Utils:

    @staticmethod
    def encode_user_password(password):
        return b64encode(password).decode()

    @staticmethod
    def generate_random_name():
        return Faker().name().replace(" ", "") + str(random.randint(1, 99))
