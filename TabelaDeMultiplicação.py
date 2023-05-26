while True:
    try:
        a = 0
        c = float(input("Coloque um número: "))
        while a <= 9:
            a = a+1
            b = c*a
            print(a,"*",c,'=',b)
    except:
        print("coloque um número real, de preferência")
