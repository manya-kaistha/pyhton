import random

# states_of_india = ["Himachal", "Kashmir", "Punjab"]
# print(states_of_india[1])
#
# states_of_india[1] = "Jammu"
# print(states_of_india)

# states_of_india.append(input("Add new state: "))
# print(states_of_india)

friends = ["Manya", "Nabhya", "Kalpana", "Mangesh"]

#first method
friend_count = len(friends)
payer = random.randint(0, friend_count - 1)

print(friends[payer])
#second method
print(random.choice(friends))