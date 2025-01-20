import re

def validate_credit_card(card_number):
    """
    Validates a credit card number using the Luhn algorithm.
    Removes non-numeric characters, checks length, and applies Luhn’s checksum.
    """
    # Remove any non-numeric characters (spaces, dashes, etc.)
    card_number = re.sub(r'\D', '', card_number)

    # Ensure the card number is exactly 16 digits long
    if len(card_number) != 16:
        return False

    # Apply Luhn algorithm for validation
    total = 0
    reversed_digits = card_number[::-1]  # Reverse the number for processing

    for i, digit in enumerate(reversed_digits):
        num = int(digit)
        if i % 2 == 1:  # Double every second digit
            num *= 2
            if num > 9:  # If the result is greater than 9, subtract 9
                num -= 9
        total += num

    return total % 10 == 0  # Valid if total is a multiple of 10

def main():
    """Handles user input and provides validation feedback."""
    card_number = input("💳 Enter your credit card number: ").strip()

    if validate_credit_card(card_number):
        print("✅ Valid credit card number!")
    else:
        print("❌ Invalid credit card number. Please check and try again.")

if __name__ == "__main__":
    main()
