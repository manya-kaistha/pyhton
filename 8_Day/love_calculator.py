def calculate_love_score(one, two):
    true = 'true'
    love = 'love'
    name = one + two

    true_count = 0
    love_count = 0
    for letter in name:
        if letter in true:
            true_count += 1

    for letter in name:
        if letter in love:
            love_count += 1

    Love_Score = str(true_count) + str(love_count)
    print(Love_Score)
