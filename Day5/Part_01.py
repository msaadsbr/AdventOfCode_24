# Open the input file and read its lines
with open("input.txt" , "r") as f :
    lines = f.readlines()

    # Split the rules and updates based on the blank line separator
    rules = lines[:lines.index("\n")]
    updates = lines[lines.index("\n") + 1 :]

    sm = 0  # Initialize sum accumulator
    for update in updates :  # Loop through each update

        # Convert the update string into a list of integers
        parts = list(map(int , update.strip().split(",")))
        c = 0  # Initialize a counter for unmatched parts

        for part in parts :  # Loop through each part in the update
            for rule in rules :  # Check the part against each rule

                # Extract the first and last values of the rule
                first , last = rule.strip().split("|")

                # Check if the part matches the rule and its pair is in the correct range
                if part == int(first) and int(last) in parts[:parts.index(part)] :
                    break
                if part == int(last) and int(first) in parts[parts.index(part) :] :
                    break
            else :
                # If no rule matched, increment the counter
                c += 1

        # If all parts are unmatched, add the middle part to the sum
        if c == len(parts) :
            sm += parts[len(parts) // 2]

    # Print the final sum
    print(sm)
