from string import ascii_letters
import random

def generate_link():
    """generate a random path"""
    return ''.join(random.choices(ascii_letters, k=8))


def recursion_generate_check(link, redis_db):
    """checks and generate link-path for uniqueness"""
    if not link:
        raise Exception('Invalid link')

    check = redis_db.get(link)

    if check:
        recursion_generate_check(link=generate_link())

    return link



