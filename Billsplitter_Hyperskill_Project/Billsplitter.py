from random import choice

print("Enter the number of friends joining (including you):")
num_people = int(input())
print()

if num_people <= 0:
    print("No one is joining for the party")
else:
    dic = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_people):
        dic[input()] = 0
    print()
    print("Enter the total bill value:")
    value = int(input())
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    print()
    if input() == "Yes":
        lucky = choice(list(dic.keys()))
        print(lucky, "is the lucky one!")
        for key in dic.keys():
            if key != lucky:
                dic[key] = round(value / (num_people-1), 2)
            else:
                dic[key] = 0
    else:
        print("No one is going to be lucky")
        for key in dic.keys():
            dic[key] = round(value / num_people, 2)
    print()
    print(dic)
