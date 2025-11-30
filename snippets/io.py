"""
Simple python script to read a json file of loan
then add perform some calculations on the data
"""
from json import load


def read_file():
    with open('loans.json', 'r') as json_file:
        data = load(json_file)
        return data


def calculate_unpaid_loans(data):
    loans = data["loans"]  # Fix: use [] not () for dict access
    unpaid_loans = [  # Fix: use [] for list, not {} for set
        loan['amount'] for loan in loans  # Fix: use ['key'] not .attribute
        if loan['status'] == "unpaid"  # Fix: correct logic and dict access
    ]
    return sum(unpaid_loans)  # Fix: sum() not sun()


def calculate_paid_loans(data):
    loans = data["loans"]  # Fix: use [] not () for dict access
    paid_loans = [
        loan['amount'] for loan in loans  # Fix: use ['key'] not .attribute
        if loan['status'] == "paid"  # Fix: use == not 'is' for comparison
    ]
    return sum(paid_loans)  # Fix: sum() not sun()


def average_paid_loans(data):
    loans = data["loans"]  # Fix: use [] not () for dict access
    paid_loans = [
        loan['amount'] for loan in loans  # Fix: use ['key'] not .attribute
        if loan['status'] == "paid"  # Fix: use == not 'is' for comparison
    ]
    sum_paid_loans = sum(paid_loans)  # Fix: sum() not sun()
    number_paid_loans = len(paid_loans)  # Fix: len() not length()
    average = (sum_paid_loans/number_paid_loans)
    return average
