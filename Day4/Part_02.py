# Function to check if the given pattern exists around (i, j) in the matrix
def check(mat, i, j):
    cond = False

    try:  # Check pattern 1: "MASS" around the center
        cond |= (mat[i-1][j-1] == "M" and mat[i-1][j+1] == "M" and mat[i][j] == "A" and mat[i+1][j-1] == "S" and mat[i+1][j+1] == "S")
    except: pass

    try:  # Check pattern 2: "MASS" rotated
        cond |= (mat[i-1][j-1] == "M" and mat[i-1][j+1] == "S" and mat[i][j] == "A" and mat[i+1][j-1] == "M" and mat[i+1][j+1] == "S")
    except: pass

    try:  # Check pattern 3: "MASS" flipped
        cond |= (mat[i-1][j-1] == "S" and mat[i-1][j+1] == "S" and mat[i][j] == "A" and mat[i+1][j-1] == "M" and mat[i+1][j+1] == "M")
    except: pass

    try:  # Check pattern 4: "MASS" mirrored
        cond |= (mat[i-1][j-1] == "S" and mat[i-1][j+1] == "M" and mat[i][j] == "A" and mat[i+1][j-1] == "S" and mat[i+1][j+1] == "M")
    except: pass
    return cond

# Initialize counter for occurrences
c = 0

# Open and read the input matrix from a file
with open("input.txt", "r") as f:
    line = f.readlines()

    # Traverse the matrix, skipping edges for boundary safety
    for i in range(1, len(line) - 1):
        for j in range(1, len(line[i].strip()) - 1):

            # Increment counter if pattern is found
            if check(line, i, j):
                c += 1

# Print the total count of patterns found
print(c)
