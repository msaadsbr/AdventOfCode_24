# Function to calculate the result for a single part based on the rules
def result_of_part(rules , parts , part) :
    before , after = 0 , 0  # Counters for matches before and after the part

    for rule in rules :  # Loop through each rule
        # Extract the first and last elements of the rule
        first , last = rule.strip().split("|")

        # Check if the current part matches the rule in the "before" direction
        if part == int(first) and int(last) in parts :
            before += 1

        # Check if the current part matches the rule in the "after" direction
        if part == int(last) and int(first) in parts :
            after += 1


    # Return the part value if the number of matches before and after are equal
    return part if before == after else 0


# Function to check if the parts list satisfies any rule
def check(rules , parts) :
    c = 0  # Counter for unmatched parts

    for part in parts :  # Loop through each part in the list
        for rule in rules :  # Check the part against each rule
            first , last = rule.strip().split("|")

            # Check if the part matches a rule in the "before" direction
            if part == int(first) and int(last) in parts[:parts.index(part)] :
                break

            # Check if the part matches a rule in the "after" direction
            if part == int(last) and int(first) in parts[parts.index(part) :] :
                break
        else :
            # Increment counter if no matching rule is found
            c += 1

    # If all parts are unmatched, return False; otherwise, return True
    if c == len(parts) :
        return False
    return True


# Open the input file and process the data
with open("input.txt" , "r") as f :
    lines = f.readlines()

    # Split the rules and updates based on the blank line separator
    rules = lines[:lines.index("\n")]
    updates = lines[lines.index("\n") + 1 :]

    sm = 0  # Initialize sum accumulator
    for update in updates :  # Loop through each update

        # Convert the update string into a list of integers
        parts = list(map(int , update.strip().split(",")))

        # Check if the parts satisfy the rules
        if check(rules , parts) :

            # If valid, calculate the sum using `result_of_part`
            for part in parts :
                sm += result_of_part(rules , parts , part)

    # Print the final sum
    print(sm)
