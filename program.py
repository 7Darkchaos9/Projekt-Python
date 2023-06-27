def findMultiple(number):
    multiple = 0
    while True:
        multiple += number
        if ifZeroAndOne(multiple):
            return multiple
        if multiple > 1_000_000_000_000:
            break
    return "BRAK"


def ifZeroAndOne(number):
    for number in str(number):
        if number not in ['0', '1']:
            return False
    return True


if __name__ == '__main__':
    tab = []
    try:
        file = open(".\\IN.txt", "r")
        file2 = open(".\\OUT.txt", "w")
    except IOError:
        print("Blad otwarcia pliku!")
        exit()

    for line in file:
        try:
            number = int(line)
            tab.append(number)
        except ValueError:
            file2.write("Znaleziono zly typ danych!")
            file2.close()
            exit()
    file.close()

    for i in tab:
        j = str(i)
        if j[-1] in ['0', '2', '4', '6', '8']:
            file2.write(str(findMultiple(i)) + "\n")
    file2.close()
