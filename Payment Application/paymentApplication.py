def process_payment(amount):
    """Simulates processing a payment transaction."""
    print(f"\n💳 Processing payment of ${amount:.2f}...")
    print("✅ Payment successful! Thank you for your transaction.\n")

def main():
    """Handles user input and validates payment amount."""
    while True:
        try:
            amount = float(input("💰 Enter payment amount: $"))
            
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
            
            process_payment(amount)
            break  # Exit loop after successful transaction
        
        except ValueError as e:
            print(f"❌ Error: {e}")
            print("🔄 Please enter a valid amount.\n")

if __name__ == "__main__":
    main()
