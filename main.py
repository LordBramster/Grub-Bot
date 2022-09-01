import json
import requests


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    j_test = json.load(open('./data/test.json'))
    print_hi(j_test['name'])
