from Log_File import logger


def add_numbers(a, b):
    return a + b


def main():

    #change push
    print("sairam")
    print("naresh")
    print("kumar")
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    total = add_numbers(a, b)
    print(f"Sum of {a} and {b} is {total}")
    logger.info("Sum of %s and %s is %s", a, b, total)
    logger.info("Sum of %s and %s is %s", a, b, total)
    logger.info("Sum of %s and %s is %s", a, b, total)
        
if __name__ == "__main__":
    main()