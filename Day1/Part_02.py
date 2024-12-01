# First Make Two Empty Lists
list1 = []
list2 = []

with open("input.txt", "r") as f:
    # Read Lines Form Input File
    lines = f.readlines()

    for line in lines :
        # Split The Singel Line Into Two Variables (After Striping From Both Sides)
        el1, el2 = line.strip().split()

        # Append The int of Both Varibales Into list1 and list2
        list1.append(int(el1))
        list2.append(int(el2))


# Initiate The Score Variable With 0
score = 0

# Loop For Every Element Of list1
for element in list1 :
    # Add Product Of element and Count Of element in list2 in score (Which Is The Main Difference From Part_01)
    score += element*list2.count(element)

# Our Answer Is In Our score Variable
print(score)
