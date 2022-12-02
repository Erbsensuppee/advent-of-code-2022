f = open("/home/quark/Documents/advent-of-code/Advent-1/calories.txt")
lines = f.readlines()
buffer = 0
result = 0
adder = 0
list1 = []
for line in lines:
    if line != '\n':
        print("Ich integer: ")
        adder = int(line) + adder
    if line == '\n':
        print("Ich leerzeichen\n")
        list1.append(adder)
        adder = 0
        print("Adder auf 0 gesetzt\n")
        #if result < adder:
        #    result = adder
        #    adder = 0
        #    print("Neues Result: ",result)
        #else:
        #    adder = 0
        #    print("Adder auf Null gesetzt.\n")  
list1.sort(reverse=True)
print("Endresult:", list1)
ele = 3
count = 0
total = 0
for i in list1:
    if count == 3:
        break
    total = i + total
    count = count + 1
print("Result der ersten 3 Elemente: ", total)

