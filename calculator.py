from decimal import Decimal


def main():
    example = input()
    elements = example.split(" ")
    fst_num = Decimal(elements[0])
    sec_num = Decimal(elements[2])
    action = elements[1]
    if action == "+":
        print(fst_num + sec_num)
    elif action == "-":
        print(fst_num - sec_num)
    elif action == "/":
        if sec_num != 0:
            print(fst_num / sec_num)
        else:
            print("Error: Division by zero.")
    elif action == "*":
        print(fst_num * sec_num)


try:
    while __name__ == '__main__':
        main()
except KeyboardInterrupt:
    print("The program has been completed")