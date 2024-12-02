# Initialize counter for "safe" sequences
safe_count = 0

# Function to check if a list is "safe"
def safe(lst):

    # Check if sorted in ascending or descending order
    if lst == sorted(lst) or lst == sorted(lst, reverse=True):

        # Ensure adjacent differences are between 1 and 3
        for i in range(len(lst) - 1):
            if not (1 <= abs(lst[i] - lst[i + 1]) <= 3):
                return False
        return True
    return False

# Read input from the file
with open("input.txt", "r") as f:
    lines = f.readlines()

# Process each line
for line in lines:
    lst = list(map(int, line.strip().split()))  # Convert line to list of integers

    if safe(lst):  # Check if the list is safe
        safe_count += 1
    else:

        # Try removing one element at a time to make the list safe
        for i in range(len(lst)):
            new_lst = lst[:i] + lst[i+1:]  # Remove element at index i

            if safe(new_lst):  # Check if modified list is safe
                safe_count += 1
                break  # Stop once a valid removal is found

# Print the total number of safe sequences
print(safe_count)
