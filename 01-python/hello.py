# My first Python script

# Variables: Python figues out the type from the value
name = "Brian"                  # str (text)
transactions_today = 42         # int (whole number)
total_amount = 18432.5          # float (decimal)
flagged = True                  # bool (True/False)

# f-strings: put variables insigt {} in a string that starts with f
print(f"Hi, I'm {name}.")
print(f"Transactions today: {transactions_today}")
print(f"Total amount: ${total_amount:,.2f}")    # :,.2f adds commas and 2 decimals

# Simple math
average = total_amount / transactions_today 
print(f"Average transaction: ${average:,.2f}")

# Check what type each variable is
print(type(name), type(transactions_today), type(total_amount), type(flagged))