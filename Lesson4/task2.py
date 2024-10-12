places = eval(input("Введите массив мест (например: [[0,1,1,0], [1,0,0,0], [0,1,0,0]]):"))
required = int(input("Введите количество мест: "))

for i, row in enumerate(places):
    places = required
    for place in row:
        if place == 0:
            places-=1
            if places == 0:
                print(i)
                exit()
        else:
            places = required

print(False)