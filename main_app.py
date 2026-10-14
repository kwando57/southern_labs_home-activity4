# Author:Kwandokuhle

import random
import datetime
import data_utils


def main():
    """
    This is the main function of the program.
    It generates transaction amounts and calculates their average.
    """
    amount1 = random.randint(50, 500)
    amount2 = random.randint(50, 500)
    amount3 = random.randint(50, 500)
    amount4 = random.randint(50, 500)
    amount5 = random.randint(50, 500)

    transaction_amounts = amount1, amount2, amount3, amount4, amount5

    today = datetime.date.today()

    average = data_utils.calculate_average(transaction_amounts)
    formatted_average = data_utils.format_currency(average)

    print("Date:", today)
    print("Generated Values:", transaction_amounts)
    print("Average:", formatted_average)


if __name__ == "__main__":
    main()

