import re

# Function to check if a string matches the "mul(x,y)" format
def is_valid_mul_format(string):
    return bool(re.match(r"^mul\(\d{1,3},\d{1,3}\)$", string))  # Matches "mul(x,y)" with x, y as 1-3 digit numbers

# Open the input file and read its content as a single string
with open("input.txt", "r") as f:
    line = f.read().strip()  # Remove leading/trailing whitespace from the file content

    score, cond = 0, True  # Initialize score to 0 and condition flag to True

    # Loop through every character in the string
    for i in range(len(line)):

        # Check if the substring matches "do()" or "don't()" and update the condition flag
        if line[i:i+4] == "do()":
            cond = True  # Enable calculation
        elif line[i:i+7] == "don't()":
            cond = False  # Disable calculation

        # Loop through substrings starting at position `i` with lengths up to 13
        for j in range(13):

            # Check if the substring is a valid "mul(x,y)" format
            if is_valid_mul_format(line[i:i+j]):

                # Extract x and y from "mul(x,y)" and split them by the comma
                elements = line[i+4:i+j-1].split(",")

                # Add x * y to the score if the condition flag is True
                score += int(elements[0]) * int(elements[1]) if cond else 0

    # Print the final calculated score
    print(score)
