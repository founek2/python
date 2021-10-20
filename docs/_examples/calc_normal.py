operator_list = ["+", "-", "/", "*", "q"]
print("Byl spuštěn program Kalkulačka, který umožnuje sčítaní, odečítání, násobení a dělení")
print("Program Vás nejprve vyzve pro zadání čísla, následně Vás vyzve pro zadání matematického operátoru (+,-,*,/), poté k dalšímu číslu")
print("Pokud následně zadáte matematický operátor, jako první operand se bude brát předešlý výsledek, pokud číslo, program Vás postupně vyzve pro zadání operátoru a poté čísla, pokud zadáte q program se ukončí")


def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


last_result = 0
while True:
    vstup = input("Zadejte vstup pro následující operaci: ")

    while vstup not in operator_list and not is_float(vstup):
        vstup = input(
            "Nezadali jste žádný podporovaný oparátor, zadejte ho znovu: ")

    if vstup in operator_list:
        operator = vstup
        operand_2 = float(input("Zadejte číslo: "))
    else:
        operand_1 = float(vstup)
        operator = input(
            "Zadejte matematický operátor, Kalkulačka umožňuje +,-,*,/ : ")
        while operator not in operator_list:
            operator = input(
                "Nezadali jste žádný podporovaný oparátor, zadejte ho znovu: ")

        # Kontrola čísla pouze tady
        operand_2 = input("Zadejte číslo: ")
        while not is_float(operand_2):
            operand_2 = input("Zadejte číslo: ")
        operand_2 = float(operand_2)

    if operator == "+":
        vysledek = operand_1 + operand_2
    elif operator == "-":
        vysledek = operand_1 - operand_2
    elif operator == "*":
        vysledek = operand_1 * operand_2
    elif operator == "/":
        vysledek = operand_1 / operand_2

    operand_1 = vysledek
    print(f"Výsledek je: {vysledek}")


print("Program byl ukončen")
