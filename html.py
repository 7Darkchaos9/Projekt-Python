import datetime


def main():
    today = datetime.date.today()
    today = today.strftime("%d_%m_%Y")
    time = datetime.datetime.now()
    time = time.strftime("%H_%M")

    try:
        inPut = open("IN.txt", "r")
        outPut = open("OUT.txt", "r")
    except IOError:
        print("Błąd otwarcia pliku.")
        return 0
    file = open(f"./raporty/{today}_{time}_raport.html", "w")

    INArray = []
    OUTArray = []

    for line in inPut:
        INArray.append(int(line))
    for line in outPut:
        OUTArray.append(int(line))
    inPut.close()
    outPut.close()

    def rows():
        for i in range(0, len(INArray)):
            file.write(f'''<tr>
            <td style="text-align: center; ">{INArray[i]}</td>
            <td style="text-align: center; ">{OUTArray[i]}</td>
        </tr>
    ''')

    htmlPage = f'''<html>
    <head>
    <title>{today}_{time}_raport</title>
    <meta charset="windows-1250">
    <style>
    table {{
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 80%;
    }}

    td, th {{
        border: 2px solid #000000;
        text-align: left;
        padding: 10px;
    }}

    </style>
    </head>
    <body>

    <center><h2>Projekt - wielokrotności zero-jedynkowe:</h2></center>

    <table align="center">
        <tr>
            <th style="text-align: center; ">Wartość Bazowa</th>
            <th style="text-align: center; ">Wartość 0-1</th>
        </tr>
    '''
    htmlPage1 = '''
    </table>

    </body>
    </html>
    '''



    file.write(htmlPage)
    rows()
    file.write(htmlPage1)

if __name__ == '__main__':
    main()