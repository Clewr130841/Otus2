tabel = {}

while True:
    vvod = input()
    if not vvod:
        break
    predmet, familiya, ocenka = vvod.split()

    if predmet not in tabel:
        tabel[predmet] = {}

    if familiya not in tabel[predmet]:
        tabel[predmet][familiya] = []

    tabel[predmet][familiya].append(ocenka)

for predmet, students in tabel.items():
    print(predmet)
    for familiya, ocenki in students.items():
        print(familiya, ' '.join(ocenki))
    print()