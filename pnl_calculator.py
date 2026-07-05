# Trade PNL Calculation


#Calculate PNL
def calculate_pnl(entry, exit_price, margin, long_position):
    if long_position:
        change_percent = ((exit_price - entry) / entry) * 100
        pnl = (change_percent * margin) / 100
    else:
        change_percent = -((exit_price - entry) / entry) * 100
        pnl = (change_percent * margin) / 100
    return change_percent, pnl

positions = []

while True:
    # User Entry Exit level
    pos_entry = float(input("Entry Price:"))
    pos_exit = float(input("Exit Price:"))
    is_long = input("Is it a long position? (yes/no): ").strip().lower() == 'yes'

    #User position Margin
    amount = float(input("Position Margin: "))
    
    change_percent, pnl = calculate_pnl(pos_entry, pos_exit, amount, is_long)

    # Display Results
    
    if pnl > 0:
        print(f"Profit: ${pnl:.2f}\nPercentage Change: {change_percent:.2f}%")
    elif pnl < 0:
        print(f"Loss: ${pnl:.2f}\nPercentage Change: {change_percent:.2f}%")
    else:
        print(f"No Profit or Loss: ${pnl:.2f}\nPercentage Change: {change_percent:.2f}%")

    positions.append(pnl)
    print(f"\nTotal Positions Calculated: {len(positions)} \nTotal PNL: ${sum(positions):.2f}")
    if input("Do you want to calculate another trade? (yes/no): ").strip().lower() != 'yes':
        break    
