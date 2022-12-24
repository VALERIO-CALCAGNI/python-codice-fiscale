# Genera codice fiscale

Script in python per calcolare il codice fiscale

il file 'listacomuni.txt' è stato scaricato da http://lab.comuni-italiani.it/download/comuni.html

## Come generare il proprio codice?

Alla fine del file mail è presente la funzione generale per il calcolo del codice
```
if __name__ == '__main__':
    cf = calcolo_cf('Mario', 'Rossi', '01-01-2000', 'M', 'Milano')
    print(f"Codice Fiscale: {cf}")
```
Per calcolare il codice, serve passare alla funzione:

+ Nome
+ Cognome
+ Data di nascita
+ Sesso
+ Comune di nascita

## Come funziona?

All'interno del file python sono presenti varie funzioni per calcolare il cf
#### funzioni per il calcolo del codice fiscale
+ calc_cognome(cognome)
+ calc_nome(nome)
+ calc_nascita(nascita, sesso)
+ calc_comune(comune)
+ calc_cod_controllo(cf)
