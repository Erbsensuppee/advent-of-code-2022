f = open("text.txt","r")
lines = f.readlines()

rockA = 'A'
paperB = 'B'
scissorC = 'C'

rockX = 'X'
paperY = 'Y'
scissorZ = 'Z'
result = 0
for line in lines:
    #print(line[0],line[1],line[2])
    if line[0] == rockA and line[2] == rockX:
        print("Rock[0] / Rock[2] = DRAW ADD 3 + 1\n")
        result = result + 4
    elif line[0] == rockA and line[2] == scissorZ:
        print("Rock[0] / Scissor[2] = Rock[0] ADD 0 + 3\n")
        result = result + 3
    elif line[0] == rockA and line[2] == paperY:
        print("Rock[0] / Paper[2] = Paper[2] ADD 6 + 2\n")
        result = result + 8
    elif line[0] == paperB and line[2] == paperY:
        print("Paper[0] / Paper[2] = DRAW ADD 3 + 2\n")
        result = result + 5
    elif line[0] == paperB and line[2] == rockX:
        print("Paper[0] / Rock[2] = Paper[0] ADD 0 + 1\n")
        result = result + 1
    elif line[0] == paperB and line[2] == scissorZ:
        print("Paper[0] / Scissor[2] = Scissor[2] ADD 6 + 3\n")
        result = result + 9
    elif line[0] == scissorC and line[2] == scissorZ:
        print("Scissor[0] / Scissor[2] = DRAW ADD 3 + 3\n")
        result = result + 6
    elif line[0] == scissorC and line[2] == rockX:
        print("Scissor[0] / Rock[2] = Rock[2] ADD 6 + 1\n")
        result = result + 7
    elif line[0] == scissorC and line[2] == paperY:
        print("Scissor [0] / Paper[2] = Paper[2] ADD 0 + 2") 
        result = result + 2
print(result)
