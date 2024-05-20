import random

# from Environment.Field import Field
# from Figures.Figure import Figure
# from Figures.Guard import Guard
# from Figures.Hunter import Hunter

if __name__ == '__main__':
    for _ in range(15):
        for __ in range(random.randint(6, 12)):
            print(chr(ord('a') + random.randint(0, 25)), end='')
        print()

