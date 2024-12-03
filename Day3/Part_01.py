import re

# Function to check if a string matches the format "mul(x,y)" where x and y are 1-3 digit numbers
def is_valid_mul_format(string):
    # Define a regex pattern for "mul(x,y)" with x and y being 1-3 digit numbers
    pattern = r"^mul\(\d{1,3},\d{1,3}\)$"

    # Check if the string matches the pattern and return True/False
    return bool(re.match(pattern, string))


# Open the file "input.txt" in read mode
with open("input.txt", "r") as f:
    # Read the entire content of the file as a single string, and strip any extra whitespace
    line = f.read().strip()

    # Initialize a variable to store the total score
    score = 0

    # Iterate through every possible starting position in the string
    for i in range(len(line)):

        # Iterate over all substring lengths from the starting position, up to 13 characters
        for j in range(13):

            # Check if the current substring matches the "mul(x,y)" format
            if is_valid_mul_format(line[i:i+j]):

                # Extract the numbers x and y from the substring
                elememts = line[i+4:i+j-1].split(",")

                # Convert the extracted numbers to integers and add their product to the score
                score += int(elememts[0]) * int(elememts[1])

    # Print the final calculated score after processing all valid "mul(x,y)" substrings
    print(score)
