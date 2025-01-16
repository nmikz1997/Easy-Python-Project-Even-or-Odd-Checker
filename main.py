def even_or_odd_checker(number):
    """
    Determines if a number is even or odd.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

# Example usage
if __name__ == "__main__":
    test_numbers = [10, 15, 0, -4, -7]
    for num in test_numbers:
        print(even_or_odd_checker(num))
