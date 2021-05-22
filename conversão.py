def exibeMsg():
    print ("\n <> Convert </>\n")

def getConvertTo():
    print("\n   F - conversão de Fahrenheit para Celsius")
    print("   C - conversão de Celsius para Fahrenheit")
    op = input("   > ")

    while op != 'c' and op != 'C' and op != 'f' and op != 'F':
        print("\n   F - conversão de Fahrenheit para Celsius")
        print("   C - conversão de Celsius para Fahrenheit")
        op = input("   > ")

    if op == 'c' or op == 'C':
        return 'c'

    else:    
        return 'f'
    
def exibeFahrenheitTOCelsius(start, end):
    i = int(start)
    n = end - start
    loop = int(n)

    print("")

    for i in range(loop+1):
        C = (start - 32) * (5 / 9)
        print("   - {:.2f}°F = {:.2f}°C".format(start, C))
        start = start + 1 
    print("")

def exibeCelsiusTOFahrenheit(start, end):
    i = int(start)
    n = end - start
    loop = int(n)
    
    print("")

    for i in range(loop+1):
        F = start * (9 / 5) + 32
        print("   - {:.2f}°C = {:.2f}°F".format(start, F))
        start = start + 1 
    print("")

def main():
    exibeMsg()

    op = getConvertTo()

    start = float(input("\n   Inicio do intervalo: ")) 
    end = float(input("   Fim do intervalo: "))

    if op == 'c':
        exibeCelsiusTOFahrenheit(start, end)

    else:    
        exibeFahrenheitTOCelsius(start, end)
 
main() 