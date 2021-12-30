import random


def create_random_list(min, max, ranger):
    empty_list = []
    for i in range(0, ranger):
        num = random.randrange(min, max)
        empty_list.append(num)
        random.shuffle(empty_list)
    return empty_list


def sort_to_list(my_list):
    while True:
        not_correct = False
        minimum = my_list[0]
        spot_of_minimum = 0
        for spot, number in enumerate(my_list):
            if minimum > number:
                not_correct = True
                my_list[spot_of_minimum] = number
                my_list[spot] = minimum

            minimum = my_list[spot]
            spot_of_minimum = spot

        if not_correct == False:
            break
    return my_list

my_list = create_random_list(50, 1000, 250)
print(my_list)
sort_to_list(my_list)
print(my_list)
