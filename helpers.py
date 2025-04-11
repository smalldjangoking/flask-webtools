import os
from string import ascii_letters
import random
import requests
from dotenv import load_dotenv

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

def request_ip_data(ip):
    """Receives Json data from ip address by API service (ipstack.com)"""
    access_key = os.getenv('IPSTACK_API')
    if not ip:
        raise Exception('Ip parameter is required')

    if not access_key:
        raise ValueError("IPSTACK_API not found")

    #delete it on production
    if ip == '127.0.0.1':
        ip = '159.224.20.200'
        load_dotenv()

    api = f"https://api.ipstack.com/{ip}/?access_key={access_key}"

    request = requests.get(api)
    response = request.json()
    return response



