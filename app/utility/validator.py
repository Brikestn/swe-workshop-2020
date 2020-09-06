import re


def validate_name(name):
    digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special = ["!", "@", "#", "$", "/", "<", ">", "-", "_", "?", "%", "^", "*"]
    space = " "
    if name == "":
        return False
    for char in name:
        if char in digit or char in special or char in space:
            return False
    return True


def validate_id(id):
    return True


def validate_phone_number(phone_number):
    return True
