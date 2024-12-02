# Firstly Make Two Empty Lists
list1 = []
list2 = []

with open("input.txt", "r") as f:
    # Read Lines Form Input File
    lines = f.readlines()

    for line in lines:

        # Split The Singel Line Into Two Variables (After Striping From Both Sides)
        el1, el2 = line.strip().split()

        # Append The int of Both Varibales Into list1 and list2
        list1.append(int(el1))
        list2.append(int(el2))

# Sort The Both Lists So That We Can Get Minimum Distances As Much As We Can
list1 = sorted(list1)
list2 = sorted(list2)

# Initiate The Score Variable With 0
score = 0

# Loop For Lenght Of Any List (Both Are Of Same Of Lenght)
for i in range(len(list1)):

    # Add abs of list1[i]-list2[i] to Score, Distance Between list1[i] and list2[i]
    score += abs(list1[i]-list2[i])

# Our Answer Is In Our score Variable
print(score)
