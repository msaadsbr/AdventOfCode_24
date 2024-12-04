# Function to count occurrences of the target code in various orientations starting at (i, j)
def possible_outcomes(line, i, j):
    cnt = 0  # Initialize counter for patterns at this position

    try:  # Check horizontal match
        hori = line[i][j:j + 4]  # Extract 4 horizontal characters
        cnt += 1 if hori == code or hori[::-1] == code else 0  # Count if match or reversed match
    except: pass

    try:  # Check diagonal match (top-left to bottom-right)
        vert = str(line[i][j] + line[i + 1][j + 1] + line[i + 2][j + 2] + line[i + 3][j + 3])
        cnt += 1 if vert == code or vert[::-1] == code else 0  # Count if match or reversed match
    except: pass

    try:  # Check diagonal match (top-right to bottom-left)
        if j >= 3:  # Ensure valid indexing for reverse diagonal
            non_diag = str(line[i][j] + line[i + 1][j - 1] + line[i + 2][j - 2] + line[i + 3][j - 3])
            cnt += 1 if non_diag == code or non_diag[::-1] == code else 0  # Count if match or reversed match
    except: pass

    try:  # Check vertical match
        diag = str(line[i][j] + line[i + 1][j] + line[i + 2][j] + line[i + 3][j])
        cnt += 1 if diag == code or diag[::-1] == code else 0  # Count if match or reversed match
    except: pass

    return cnt  # Return the count of matches for this position


# Initialize counter for total occurrences
c = 0

# Set the target code to detect
code = "XMAS"

# Open and read the input matrix from a file
with open("input.txt", "r") as f:
    lines = f.readlines()

    # Traverse every position in the matrix
    for i in range(len(lines)):
        for j in range(len(lines[i].strip())):  # Use strip to avoid trailing spaces

            # Add counts from possible outcomes starting at (i, j)
            c += possible_outcomes(lines, i, j)

# Print the total count of patterns found
print(c)
