def result_of_part(rules , parts , part) :
    before , after = 0 , 0
    
    for rule in rules :
        first , last = rule.strip().split("|")

        if part == int(first) and int(last) in parts :
            before += 1

        if part == int(last) and int(first) in parts :
            after += 1


    return part if before == after else 0


def check(rules , parts) :
    c = 0

    for part in parts :
        for rule in rules :
            first , last = rule.strip().split("|")

            if part == int(first) and int(last) in parts[:parts.index(part)] :
                break

            if part == int(last) and int(first) in parts[parts.index(part) :] :
                break
        else :
            c += 1

    if c == len(parts) :
        return False
    return True


with open("input.txt" , "r") as f :
    lines = f.readlines()

    rules = lines[:lines.index("\n")]
    updates = lines[lines.index("\n") + 1 :]

    sm = 0
    for update in updates :

        parts = list(map(int , update.strip().split(",")))

        if check(rules , parts) :

            for part in parts :
                sm += result_of_part(rules , parts , part)

    print(sm)
