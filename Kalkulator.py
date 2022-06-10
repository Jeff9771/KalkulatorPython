while True:
    a = float(input("Podaj A: "))
    b = float(input("Podaj B: "))
    print("działania: , + , - , * , / , ^2")
    dzialanie = input("Jakie działanie chcesz wykonać na podanych liczbach")
    if dzialanie == "+":
        print(a, ' + ', b, "=", a + b)
    elif dzialanie == "-":
        print(a, ' - ', b, "=", a - b)
    elif dzialanie == "*":
        print(a, ' * ', b, "=", a * b)
    elif dzialanie == "/":
        print(a, ' / ', b, "=", a / b)
    elif dzialanie == "^2":
        print(a, ' ^2 ', b, "=", a ** b)
    else:
        print("Nie znam znaku: \"", dzialanie, "\"" "  :c")
    koniec = input("wpisz \"koniec\" jeśli chcesz zakończyć działanie kalkulatora jeśli nie kontynuuj")
    if koniec == "koniec":
        break


