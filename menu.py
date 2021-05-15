import subprocess

def menu():
    print(('-'*12) + 'Menu'+ ('-' *12))
    print('1. Send emails for each item')
    print('2. Send one email for all items')
    print('Q. Exit')
    print('-'*28)
    return input(': ')
