# Trade PNL Calculation

while True:
    # User Entry Exit level
    pos_entry = float(input("Entry Price:"))
    pos_exit = float(input("Exit Price:"))
    is_long = input("Is it a long position? (yes/no): ").strip().lower() == 'yes'

    #User position Margin
    amount = float(input("Position Margin: "))

    #Calculate PNL
    change_percent = abs(((pos_exit - pos_entry) / pos_entry) * 100)
    pnl = abs((change_percent * amount) / 100)

    # Display Results

    if is_long:
        if pos_exit > pos_entry:
            print(f"Profit: ${pnl:.2f}\nPercentage Change: {change_percent:.2f}%")
        elif pos_exit < pos_entry:
            print(f"Loss: ${pnl:.2f}\nPercentage Change: {change_percent:.2f}%")
        else:
            print(f"No Profit or Loss: ${pnl:.2f}\nPercentage Change: {change_percent:.2f}%")
    else:
        if pos_exit < pos_entry:
            print(f"Profit: ${pnl:.2f}\nPercentage Change: {change_percent:.2f}%")
        elif pos_exit > pos_entry:
            print(f"Loss: ${pnl:.2f}\nPercentage Change: {change_percent:.2f}%")
        else:
            print(f"No Profit or Loss: ${pnl:.2f}\nPercentage Change: {change_percent:.2f}%")

    if input("Do you want to calculate another trade? (yes/no): ").strip().lower() != 'yes':
        break    