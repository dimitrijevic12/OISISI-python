import obilazakFajlova
import queryParser
import searchAlgorithm

bool1 = '1'
bool2 = '1'
while bool1 == '1':
    if bool2 == '1':
        while True:
            rootdir = input("Unesite korenski direktorijum: ")
            (bool, root) = obilazakFajlova.obidji(rootdir)
            if bool == True:
                break
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
            print(konacanSet)
            print(recnikStranica)
        print('**********************************************************************\n')
        print('Ako zelite da unesete novi korenski direktorijum, unesite broj 1\nAko zelite ponovo da unesete upit, unesite broj 2\nAko zelite da izadjete iz programa, unesite broj 3')
        print('\n**********************************************************************\n')
        bool2 = input('Opcija: ')
    elif bool2 == '3':
        bool1 = '3'
    else:
        bool2 = input("Unesite jednu od opcija(1, 2, 3): ")

