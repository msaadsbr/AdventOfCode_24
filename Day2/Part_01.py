# Initialize a counter for "safe" sequences
safe_count = 0

# Open and read all lines from the input file
with open("input.txt", "r") as f:
    lines = f.readlines()

# Process each line from the file
for line in lines:

    # Convert the line into a list of integers
    lst = list(map(int, line.strip().split()))

    # Check if the list is sorted in ascending or descending order
    if lst == sorted(lst) or lst == sorted(lst, reverse=True):

        # Verify if all adjacent differences are between 1 and 3
        for i in range(len(lst) - 1):
            if not (1 <= abs(lst[i] - lst[i + 1]) <= 3):
                break

        else:  # If no break, the sequence is safe
            safe_count += 1

# Output the total count of safe sequences
print(safe_count)
