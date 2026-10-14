# Author:Kwandokuhle

import data_utils
import random
import datetime


def main():
    """
    This is the main function of the program.
    It generates transaction amounts and calculates their average.
    """

    transaction_amounts = []

    amount = random.randint(50, 500)
    transaction_amounts.append(amount)

    amount = random.randint(50, 500)
    transaction_amounts.append(amount)

    amount = random.randint(50, 500)
    transaction_amounts.append(amount)

    amount = random.randint(50, 500)
    transaction_amounts.append(amount)

    amount = random.randint(50, 500)
    transaction_amounts.append(amount)

    today = datetime.date.today()

    average = data_utils.calculate_average(transaction_amounts)

    formatted_average = data_utils.format_currency(average)

    print("Date:", today)
    print("Generated Values:", transaction_amounts)
    print("Average:", formatted_average)


if __name__ == "__main__":
    main()

