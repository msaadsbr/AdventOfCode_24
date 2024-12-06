with open("input.txt" , "r") as f :
    lines = f.readlines()

    rules = lines[:lines.index("\n")]
    updates = lines[lines.index("\n") + 1 :]

    sm = 0
    for update in updates :

        parts = list(map(int , update.strip().split(",")))
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
            sm += parts[len(parts) // 2]

    print(sm)
