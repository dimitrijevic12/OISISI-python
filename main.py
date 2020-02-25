from obilazakDokumenata import obilazakFajlova
from parseri import queryParser
from pretragaDokumenata import searchAlgorithm
import time
from ispis import paginacija
from ispis import rangiranje

bool1 = '1'
bool2 = '1'
while bool1 == '1':
    if bool2 == '1':
        while True:
            rootdir = input("Unesite korenski direktorijum: ")
            beginning = time.time()
            (bool, root,graf) = obilazakFajlova.obidji(rootdir)

            ending = time.time()
            tik = ending - beginning

            if bool:  # &tacno:

                print("Uspesno su parsirana dokumenta. \n")
                print("Vreme za parsiranje je bilo: \n", tik, " \n")
                break

            else:

                print("Neuspesno su parsirana dokumenta. \n")
                print("Vreme za pokusaj parsiranja je bilo: \n", tik, " \n")

        print('**********************************************************************\n')
        print('Ako zelite ponovo da unesete korenski direktorijum, unesite broj 1\nAko zelite da unesete upit, unesite broj 2\nAko zelite da izadjete iz programa, unesite broj 3')
        print('\n**********************************************************************\n')
        bool2 = input('Opcija: ')
    elif bool2 == '2':
        bool3 = False
        while not bool3:
            query = input("Unesite upit: ")
            (bool3, logop, search) = queryParser.parse(query)

        (konacanSet, recnikStranica) = searchAlgorithm.find(root, search, logop)

        print('\n**********************************************************************\n')


        if not recnikStranica:
            print('Nije pronadjena nijedna rec!\n')
        else:
            #print(konacanSet)
            #print(recnikStranica)

            lista = rangiranje.rangiraj(graf, recnikStranica)

            print('***************************RANGIRANJE*********************************\n')
            if not recnikStranica:
                print('Rangiranje neuspesno!\n')
            else:
                paginacija.paginacija(lista)
        print('\n**********************************************************************\n')
        print('Ako zelite da unesete novi korenski direktorijum, unesite broj 1\nAko zelite ponovo da unesete upit, unesite broj 2\nAko zelite da izadjete iz programa, unesite broj 3')
        print('\n**********************************************************************\n')
        bool2 = input('Opcija: ')
    elif bool2 == '3':
        bool1 = '3'
    else:
        bool2 = input("Unesite jednu od opcija(1, 2, 3): ")


