import random
def swap_random(list):
    for i in range(len(list)):
        j = random.randint(0, len(list) - 1)
        list[i], list[j] = list[j], list[i]
    return list
x=["red","blue","green","yellow","black"]
print(swap_random(x))