"""utils/test_data.py -- Centralised test constants. Never hardcode in tests."""


class Users:
    STANDARD    = {"username": "standard_user",            "password": "secret_sauce"}
    LOCKED_OUT  = {"username": "locked_out_user",          "password": "secret_sauce"}
    PROBLEM     = {"username": "problem_user",              "password": "secret_sauce"}
    PERFORMANCE = {"username": "performance_glitch_user",   "password": "secret_sauce"}


class CheckoutInfo:
    VALID = {"first": "John", "last": "Smith", "zip_code": "M5V 2T6"}


class Messages:
    LOCKED_OUT_ERROR = "Epic sadface: Sorry, this user has been locked out."
    EMPTY_USER_ERROR = "Epic sadface: Username is required"
    EMPTY_PASS_ERROR = "Epic sadface: Password is required"
    FIRST_NAME_REQ   = "Error: First Name is required"
    LAST_NAME_REQ    = "Error: Last Name is required"
    POSTAL_CODE_REQ  = "Error: Postal Code is required"
    ORDER_CONFIRMED  = "Thank you for your order!"


class Products:
    TOTAL_COUNT = 6
