import random
student_score = [12, 34, 45, 45, 45,  54, 45, 45, 4, 45, 44, 5, 54]

new_student_score = []

for i in student_score:
    rand = random.randint(1, 9)
    i += rand
    new_student_score.append(i)

old_max = max(new_student_score)
print(old_max)

max = -1
for i in new_student_score:
    if i > max:
        max = i

print(max)

