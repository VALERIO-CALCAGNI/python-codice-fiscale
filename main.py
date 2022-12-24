import pandas as pd

vocali = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

lettere_mesi = {'01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E', '06': 'H',
                '07': 'L', '08': 'M', '09': 'P', '10': 'R', '11': 'S', '12': 'T'}

cod_dispari = {'0': 1, '1': 0, '2':5, '3': 7, '4': 9, '5': 13,'6': 15, '7': 17,
               '8': 19, '9': 21, 'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9, 'F': 13,
               'G': 15, 'H': 17, 'I':19, 'J': 21, 'K': 2, 'L': 4, 'M': 18, 'N': 20,
               'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14, 'U': 16, 'V': 10,
               'W': 22, 'X': 25, 'Y': 24, 'Z': 23}

cod_pari = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
            'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
            'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
            'Y': 24, 'Z': 25}


def calcolo_cf(nome, cognome, nascita, sesso, comune):

    cf = calc_cognome(cognome)
    cf += calc_nome(nome)
    cf += calc_nascita(nascita, sesso)
    cf += calc_comune(comune)
    cf += calc_cod_controllo(cf)

    return cf.upper()


def calc_cognome(cognome):
    cons = []
    voc = []
    for i in cognome:
        if i not in vocali:
            cons.append(i)
        else:
            voc.append(i)
    cod = "".join(cons + voc +['x']*2)[0:3] #Nel caso in cui un cognome abbia meno di tre lettere, la parte di codice viene completata aggiungendo la X (per esempio: Fo → FOX)

    return cod


def calc_nome(nome):
    cons = []
    voc = []
    for i in nome:
        if i not in vocali:
            cons.append(i)
        else:
            voc.append(i)

    # se il nome contiene quattro o più consonanti, si scelgono la prima, la terza e la quarta (es: Gianfranco → GFR)
    if len(cons) > 3:
        cons[1:2] = []

    cod = "".join(cons + voc + ['x']*2)[0:3]
    return cod


def calc_nascita(nascita, sesso):
    giorno, mese, anno = nascita.split('-')

    ultime_cifre_anno = anno[-2:len(anno)]

    if len(giorno) == 1:     # aggiungere lo zero davanti ai numeri ad una cifra
        giorno = f"0{giorno}"

    if sesso == 'F':
        giorno = int(giorno) + 40

    return ultime_cifre_anno + lettere_mesi[mese] + str(giorno)


def calc_comune(comune):
    data = pd.read_csv('listacomuni.txt', delimiter=';', encoding='cp1252')

    if comune.isdigit():
        d = data.loc[data.CAP == comune]
    else:
        d = data.loc[data.Comune == comune]

    if d.empty:
        print("ERRORE calcolo codice comune, controlla se hai scritto correttamente")
        return 'ERR'

    return d['CodFisco'].values[0]


def calc_cod_controllo(cf):
    somma = 0
    cf = cf.upper()

    for i, elem in enumerate(cf):
        if i%2 ==0:
            somma += cod_pari[elem]
        else:
            somma += cod_dispari[elem]

    return chr(ord('a')+(somma%26))


if __name__ == '__main__':
    cf = calcolo_cf('Mario', 'Rossi', '01-01-2000', 'M', 'Milano')
    print(f"Codice Fiscale: {cf}")
