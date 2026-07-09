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
winrate_count = 0

while True:
    # User Entry Exit level
    try:
        pos_entry = float(input("Entry Price:"))
    except ValueError:
        print("Invalid entry price. Please enter a valid number.")
        continue

    try:
        pos_exit = float(input("Exit Price:"))
    except ValueError:
        print("Invalid exit price. Please enter a valid number.")
        continue

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

    positions.append({"entry": pos_entry, "exit": pos_exit, "is_long": is_long, "pnl": pnl})
    print(f"\nTotal Positions Calculated: {len(positions)} \nTotal PNL: ${sum([pos['pnl'] for pos in positions]):.2f}")
    if input("Do you want to calculate another trade? (yes/no): ").strip().lower() != 'yes':
        break    
for winrate in positions:
    if winrate['pnl'] > 0:
        winrate_count += 1
print(f"Win Rate: {(winrate_count/len(positions))*100:.2f}% ({winrate_count}/{len(positions)} trades)")

with open("trade_history.txt", "w") as f:
    for pos in positions:
        f.write(f"Entry: {pos['entry']}, Exit: {pos['exit']}, Long Position: {pos['is_long']}, PNL: {pos['pnl']:.2f}\n")