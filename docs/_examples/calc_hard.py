texts = ["Zadejte první číslo: ", "Zadejte matematický operátor: ", "Zadejte druhé číslo: "]
allowed_operators = ['+', '-', '/', '*', '**', '%']

def calculate(value_list):
    num1, operator, num2 = value_list

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2


last_result = None
while True:

    values = []
    i = 0
    while i < 3:
        value = input("Zadej hodnotu: ")

        if value == "q":    # ukončení programu
            exit(0)

        # pokud je zadán operátor, tak zachovat řetězec,
        # jinak převést na číslo
        if value in allowed_operators:
            values.append(value)
        else:
            values.append(float(value))


        # pokud je zadán operátor jako první, tak
        # kontrola jestli existuje minulý výsledek
        # pokud ano, tak ho přidat jako první číslo
        # do pole hodnot -> Důvod? Abychom mohli využít
        # stejný kód pro výpočet v obou případech
        if value in allowed_operators and i == 0:
            if last_result == None:     # pokud není poslední výsledek -> zeptat znovu na hodnotu
                print("Předchozí výpočet neexistuje")
                continue
            else:
                values.insert(0, last_result)
                i += 1      # v poli již máme operátor a insert přídal první číslo na pozici 0 -> již potřebujeme pouze jednu hodnotu načíst
        i += 1
    
    print(values)

    result = calculate(values)

    print(f'Výsledek: {result}')
    last_result = result