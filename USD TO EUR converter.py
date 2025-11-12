from forex_python.converter import CurrencyRates
c = CurrencyRates()
while True:
    print("1. USD TO EUR.\n2. EUR TO USD.\n3. Exit.")
    try:
        choice = int(input("\nEnter Your Choice: "))
        if choice == 1:
            base_currency = 'USD'
            target_currency = 'EUR'
            USD_Amount = float(input("Enter the amount you wished to convert: "))
            converted_amount = c.convert(base_currency,target_currency, USD_Amount)
            print(f"{USD_Amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")

        elif choice == 2:
            base_currency = 'EUR'
            target_currency = 'USD'
            EUR_Amount = float(input("Enter the amount you wished to convert: "))
            converted_amount = c.convert(base_currency,target_currency, EUR_Amount)
            print(f"{EUR_Amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")

        elif choice == 3:
            print('Exiting... ')
            break
        else:
            print("\nInvalid Choice. Please enter a valid choice. ")
    except ValueError:
            print("\nInvalid Choice. Please enter a valid choice. ")




