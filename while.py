# Initialize variables
total = 0
count = 0

# Continually ask users to enter a number
while True:
    num = float(input("Enter a number (enter -1 to stop): "))
    
    # Check if the number is -1 to stop the loop
    if num == -1:
        break
    
    # Add the number to the total and increment the count
    total += num
    count += 1

# Check if any numbers were entered (excluding -1) to avoid division by zero
if count > 0:
    # Calculate the average of numbers entered (excluding -1)
    average = total / count
    print("Average of numbers entered:", average)
else:
    print("No numbers entered (excluding -1)")