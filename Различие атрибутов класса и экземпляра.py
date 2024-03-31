class Building:
    total = 0

    def __init__(self):
        Building.total += 1


buildings = [Building() for _ in range(40)]

print("Общее количество созданных зданий:", Building.total)
