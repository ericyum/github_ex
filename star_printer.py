def draw_pattern_1(rows=6):
    """
    Draws a right-angled triangle of stars.
    *
    **
    ***
    ****
    *****
    ******
    """
    print("--- Pattern 1 ---")
    for i in range(1, rows + 1):
        print('*' * i)
    print("\n")


def draw_pattern_2_and_3(rows=6):
    """
    Draws a pyramid of stars.
         *
        ***
       *****
      *******
     *********
    ***********
    """
    print("--- Pattern 2 & 3 ---")
    for i in range(1, rows + 1):
        # Calculate spaces for centering
        spaces = ' ' * (rows - i)
        # Calculate stars
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print("\n")


def draw_pattern_4(half_height=5):
    """
    Draws a diamond shape of stars.
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
    """
    print("--- Pattern 4 ---")
    # Top half of the diamond
    for i in range(1, half_height + 1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    
    # Bottom half of the diamond
    for i in range(half_height - 1, 0, -1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print("\n")


def draw_pattern_5(half_height=5):
    """
    Draws an hourglass shape of stars.
    *********
     *******
      *****
       ***
        *
       ***
      *****
     *******
    *********
    """
    print("--- Pattern 5 ---")
    # Top half of the hourglass
    for i in range(half_height, 0, -1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
        
    # Bottom half of the hourglass
    for i in range(2, half_height + 1):
        spaces = ' ' * (half_height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print("\n")


def draw_pattern_6():
    """
    Draws a complex tree-like pattern.
    The structure is complex, so it's printed line by line.
    """
    print("--- Pattern 6 ---")
    pattern = [
        "    *",
        "   ***",
        "  *****",
        " *******",
        "*********",
        "   ***   ",
        "  *****  ",
        " ******* ",
        "*********"
    ]
    # A different interpretation of the 6th pattern from the image is below
    # This one seems more faithful to the image provided.
    pattern_6_visual = [
        "      *",
        "     ***",
        "    *****",
        "   *******",
        "  *********",
        " ***********",
        "      *",
        "      *",
        "  *********",
        " ***********",
        "*************"
    ]
    # The most accurate representation of the 6th image
    pattern_6_final = [
        "     *",
        "    ***",
        "   *****",
        "  *******",
        " *********",
        "***********",
        "    ***",
        "    ***"
    ]
    # The pattern in the image is ambiguous. I will select one final version
    # that is a common tree shape.
    print("     *")
    print("    ***")
    print("   *****")
    print("  *******")
    print(" *********")
    print("***********")
    print("    ***")
    print("    ***")
    print("\n")


if __name__ == "__main__":
    draw_pattern_1()
    draw_pattern_2_and_3()
    draw_pattern_4()
    draw_pattern_5()
    draw_pattern_6()
