#Author: Kwandokuhle

"""
This file contains functions for formatting currency and calculating averages
"""


def calculate_average(numbers_list):
    """
    This function calculates the average of a list of numbers

    :param numbers_list: The list of numbers
    :return: Returns the average
    """
    total = numbers_list[0] + numbers_list[1] + numbers_list[2] + numbers_list[3] + numbers_list[4]
    average = total / 5
    return average


def format_currency(amount):
    """
    This function formats an amount as Rands

    :param amount: Amount to format
    :return: Amount formatted as Rands
    """
    formatted_amount = "R" + str(round(amount, 2))
    return formatted_amount




