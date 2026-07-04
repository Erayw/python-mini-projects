# Trade PNL Calculation


#Calculate PNL
def calculate_pnl(entry, exit_price, margin, long_position):
    change_percent = abs(((exit_price - entry) / entry) * 100)
    pnl = abs((change_percent * margin) / 100)
    return change_percent, pnl


while True:
    # User Entry Exit level
    pos_entry = float(input("Entry Price:"))
    pos_exit = float(input("Exit Price:"))
    is_long = input("Is it a long position? (yes/no): ").strip().lower() == 'yes'

    #User position Margin
    amount = float(input("Position Margin: "))
    
    change_percent, pnl = calculate_pnl(pos_entry, pos_exit, amount, is_long)

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
