for i in range(120, 500, 3):
    if i % 3 == 0:
        print("იყოფა სამზე ", i)
    elif i % 5 == 0:
        print("იყოფა ხუთზე ", i)
    elif i % 7 == 0:
        print("იყოფა შვიდზე ", i)
    else:
        print(i)