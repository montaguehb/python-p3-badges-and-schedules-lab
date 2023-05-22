def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(n) for n in names]

def assign_rooms(names):
    newList = []
    x = 1
    for n in names:
        newList.append(f"Hello, {n}! You'll be assigned to room {x}!")
        x += 1
    return newList

def printer(names):
    for n in batch_badge_creator(names):
        print(n)
    for n in assign_rooms(names):
        print(n)
