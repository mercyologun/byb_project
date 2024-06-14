# Define the number of rows for the pattern
num_rows = 9

# Iterate over each row
for i in range(1, num_rows + 1):
    if i <= (num_rows + 1) // 2:
        # Print increasing number of stars for the first half of the pattern
        print('*' * i)
    else:
        # Print decreasing number of stars for the second half of the pattern
        print('*' * (num_rows - i + 1))