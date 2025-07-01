def print_pattern1(rows=5):
    print("Pattern 1:")
    for i in range(1, rows + 1):
        print("*" * i)
    print()

def print_pattern2(rows=5):
    print("Pattern 2:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)
    print()

def print_pattern3(rows=5):
    print("Pattern 3:")
    for i in range(rows, 0, -1):
        print("*" * i)
    print()

def print_pattern4(rows=5):
    print("Pattern 4:")
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * i)
    print()

def print_pattern5(rows=5):
    print("Pattern 5:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    print()

def print_pattern6(rows=5):
    print("Pattern 6:")
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    print()

def print_pattern7(rows=5):
    print("Pattern 7:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    print()

def print_pattern8(rows=5):
    print("Pattern 8:")
    for i in range(1, rows + 1):
        print("*" * i + " " * (2 * (rows - i)) + "*" * i)
    for i in range(rows - 1, 0, -1):
        print("*" * i + " " * (2 * (rows - i)) + "*" * i)
    print()

def print_pattern9(rows=5):
    print("Pattern 9:")
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(2, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    print()

if __name__ == "__main__":
    print_pattern1()
    print_pattern2()
    print_pattern3()
    print_pattern4()
    print_pattern5()
    print_pattern6()
    print_pattern7()
    print_pattern8()
    print_pattern9()
