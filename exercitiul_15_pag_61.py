nume=input('Dati numele:')
if nume.isalpha()==True:
    if nume.istitle()==True:
        print('CORECT')
    else:
        print('INCORECT')   
else:
    print('INCORECT')