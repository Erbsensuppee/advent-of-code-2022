f = open("text.txt","r")
lines = f.readlines()

rockA = 'A'
paperB = 'B'
scissorC = 'C'

loseX = 'X'
drawY = 'Y'
winZ = 'Z'
result = 0
for line in lines:
    if line[0] == rockA and line[2] == loseX:
        print("rock[0] / loseX = Scissor[2] ADD 0 + 3")
        result = result + 3
    elif line[0] == rockA and line[2] == drawY:
        print("rock[0] / drawY = Rock[2] ADD 3 + 1")
        result = result + 4
    elif line[0] == rockA and line[2] == winZ:
        print("rock[0] / winZ = Paper[2] ADD 6 + 2")
        result = result + 8
    elif line[0] == paperB and line[2] == loseX:
        result = result + 0 + 1
    elif line[0] == paperB and line[2] == drawY:
        result = result + 3 + 2
    elif line[0] == paperB and line[2] == winZ:
        result = result + 6 + 3
    elif line[0] == scissorC and line[2] == loseX:
        result = result + 0 + 2
    elif line[0] == scissorC and line[2] == drawY:
        result = result + 3 + 3
    elif line[0] == scissorC and line[2] == winZ:
        result = result + 6 + 1
print(result)