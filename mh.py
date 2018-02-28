num=10
people=[]
for i in range(num):
    people.append(i)
print(people)

def tt(people):
    while len(people)==1:
        for x in people:
            if (x+1)%3==0:
                del people[x+1]
tt(people)
print(people)
master0