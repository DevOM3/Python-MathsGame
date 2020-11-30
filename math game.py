import random
import time

op1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
op = ["+", "-", "*", "/"]
op2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data = []
score = []
player = 0
q = 1

players = int(input("Enter the no of players :- \t"))

for i in range(0, players):
    names = input(f"Player no {i+1} enter your name :- \t")
    data.append(names)

print("Let's get started !!!")

while True:
    if q == 6:
        player = player + 1
        t2 = time.clock()
        score.append(t2 - t1)
        q = 1
        print(f"{data[player - 1]} you took {t2 - t1} seconds to perform this")
    if player == players:
        break
    print(f"For {data[player]}")

    t1 = time.clock()
    first = random.choice(op1)
    operator = random.choice(op)
    second = random.choice(op2)

    print(f"Question no. {q} :- \t")
    print(first, " ", operator, " ", second)
    while True:
        ans = int(input())
        if operator == '+':
            if ans == (first + second):
                print("Right answer .... ")
                q = q + 1
                break
            else:
                print("Solve again")
                continue
        elif operator == '-':
            if ans == (first - second):
                print("Right answer .... ")
                q = q + 1
                break
            else:
                print("Solve again")
                continue
        elif operator == '*':
            if ans == (first * second):
                print("Right answer .... ")
                q = q + 1
                break
            else:
                print("Solve again")
                continue
        elif operator == '/':
            if ans == int(first / second):
                print("Right answer .... ")
                q = q + 1
                break
            else:
                print("Solve again")
                continue


for i in range(0, players):
    print(f"The score of {data[i]} is {score[i]}")
