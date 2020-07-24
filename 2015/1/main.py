f = open("input", "r").read()
f = f[:-1] # remove trailing char

floor = 0
position = 1
entered_basement = False

for i in f:
    if i == '(':
        floor = floor + 1
    else:
        floor = floor - 1
    if (floor < 0) and (entered_basement == False):
        print('entering basement on move ' + str(position))
        entered_basement = True

    position = position + 1

print(floor)