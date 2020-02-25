import math


def paginacija(lista=list):
    a = len(lista)
    i = 0
    print('Pronasli smo ' + str(len(lista)) + ' stranica koje sadrze trazenu rec')
    br_html_strana = 1
    while br_html_strana > 0:
        while True:
            try:
                m = input('Unesite broj strana za prikaz ili unesite nulu za povratak u meni: ')
                br_html_strana = int(m)
                if br_html_strana<(a+1) and br_html_strana>-1:
                    break
                else:
                    print('Broj strana za prikaz mora biti pozitivan ceo broj koji je manji od ' + str(len(lista)+1))
            except ValueError:
                print('Broj strana za prikaz mora biti pozitivan ceo broj koji je manji od '+str(len(lista)+1))
        if br_html_strana != 0:
            broj_stranica = math.ceil(a / br_html_strana)
            for l in lista:
                if i < br_html_strana:
                    print((i + 1), end='')
                    ispis(l)
                    i += 1
                else:
                    break
            print('Trenutno je prikazana prva strana ')
            trenutna = 1
            while int(trenutna) > 0:

                while True:
                    try:
                        c = input('Unesite broj od 1 do ' + str(broj_stranica) + ' zavisno od toga koju stranu zelite da prikazete ili unesite nulu za promenu broja prikazanih rezultata :')
                        trenutna= int(c)
                        if trenutna < (broj_stranica+ 1) and trenutna > -1:
                            break
                        else:
                            print('Broj strana za prikaz mora biti pozitivan ceo broj koji je manji od ' + str(broj_stranica+1))
                    except ValueError:
                        print('Broj strana za prikaz mora biti pozitivan ceo broj koji je manji od ' + str(broj_stranica+1))

                j = 1
                k = 1
                i = 0
                redni_br = 0
                for l in lista:
                    if k == int(trenutna):
                        if i < br_html_strana:
                            print((redni_br + 1), end='')
                            ispis(l)
                            redni_br += 1
                            i += 1
                        else:
                            break
                    else:
                        if j < br_html_strana:
                            j += 1
                            redni_br += 1
                        else:
                            k += 1
                            j = 1
                            redni_br += 1
        else:
            break


def ispis(element):
    print('. ' + element[0] + ' rang: ' + str(element[1]) + ' (' + str(element[2]) + ',' + str(element[3]) + ',' + str(
        element[4]) + ')')
