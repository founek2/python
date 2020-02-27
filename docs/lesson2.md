# 2. Lekce

## List
Dalším důležitým datovým typem je List (v jiných jazycích známí jako pole). V tomto typu lze uložit libovolné množství dat, která spolu často nějak souvisí ale nemusí, a následně na ně přistupovat pomocí indexů. S tímto přístupem jsme se již setkali při přistupování na jednotlivá písmena v řetězci. Výhoda je že pro tisíc hodnot nemusíme mít tisíc promněných ale pouze jednu typu List a jednotlivé hodnoty jsou přistupné pomocí indexů. Příklad použití:
```python
promnena = [14, 20, 10, 1, 60, "Kitty", -0.24]      # Do listu lze ukládat současně hodnoty různých typů
          #  └──index začíná na 0

promnena[0]     # -> 14
promnena[5]     # -> "Kitty"

for prvek in promnena:
    print(prvek)        # -> bude vypisovat jednotlivé prvky od nultého indexu až po poslední

promnena.append("Hello")    # přidá nový prvek na konec listu
# promnena = [14, 20, 10, 1, 60, "Kitty", -0.24, "Hello"] 

promnena.pop()    # Odebere poslední prvek
# promnena = [14, 20, 10, 1, 60, "Kitty", -0.24] 
```


## Tuple
Datový typ tuple není nic jiného než n-tice. Lze si ho představit jako list, které pokud je jednou vytvořen, tak nelze měnit jeho prvky ani je přidávat či odebírat. Pro procházení lze využít stejný způsob jako u listu.
```python
ntice = (14, 20, 10, 1, 60, "Kitty", -0.24)      # Do listu lze ukládat současně hodnoty různých typů
      #  └──index začíná na 0

ntice[0]     # -> 14
ntice[5]     # -> "Kitty"

for prvek in ntice:
    print(prvek)        # -> bude vypisovat jednotlivé prvky od nultého indexu až po poslední
```

### 2.1.x Cvičení na pole
* Vytvořte promněnou s prázdnám polem a vložte do něj prvky 0 až 99 (nedělejte to manuálně, ale použijte cyklus). Následně vypište každý třetí prvek.
* Vytvořte pole s alespoň 10 čísly a následně spočítejte průměr hodnot

## Funkce pokračování
V první lekci jsme si ukázali jak funkci zavolat, nyní si ukáže jak si můžeme vytvořit svoji vlastní. Používá se pro to klíčové slovo `def`, za kterým následuje název naší funkce a v závorkách názvy promněných do která se nám vloží argumentu, pokud naší funkci někdo zavolá.
```python
def kill_program(id, reasson):
    print(f'program with id: {id} was killed')
    print(f'Reason for kill: {reasson}')

    for i in range(15):
        ... # some black magic

    return True         # návratová hodnota

kill_program(2, 'I don`t like it')
```
Všimněte si slova `return` na konci funkce. Každá funkce může vracet nějakou hodnotu, co vrátí je hodnota za slovem return. Příklad použtí:
```python
outcome = kill_program(1, 'Too high memory usage')

if outcome == True:
    print('Successfully killed')
else:
    print('Unable to kill')
```

### 2.2.x Cvičení funkce
* napište funkci `add`, která vezme dva argumenty a vrátí jejich součet
```add(4, 6) -> 10```
* napište funkci `show` která vypíše obsah pole do terminálu, které dostane jako parametr
```python
numbers = [1, 2, 4]
show(numbers) # -> nic nemusí vracet
```

### 2.2.3 Výpočet součtu
Napište program, který se uživatele bude dokola ptát na číslo. Toto číslo budete přičítat k dosavadnímu celkovému součtu předchozích čísel. (Využijte předchozí funkci add, kterou jste si napsali)

### 2.2.4 Statistika pole
Napište tyto 3 funkce:
* `inc` - parametr dostane list čísel a její úkol je přičíst ke každému číslu 1 a list vrátit
* `maxList` - parametr dostane pole čísel a vrátí maximum
* `minList` - parametr dostane pole čísel a vrátí minimum
* `sumList` - parametr dostane pole čísel a vrátí součet
Vytvořte skript, který se zeptá uživatele na čísla oddělená čárkou. Načte vstup jako string, potom pomocí metody `split` převede na list a následně vypíše zajímavé statistiky v tomto formátu:
```text
min: {minimální prvek}
max: {maximální prvek}
sum: {součet}
inc: {list s hodnotami zvětšenými o 1}
orig: {list s původními hodnotami}
```

### 2.2.5 Kalkulačka podruhé
Program se zeptá na číslo, operátor, číslo -> ověří že čísla jsou čísla a operátor je známý operátor (pokud operátor neznáme, tak vypíšeme hlášku "neznámý operátor" a zeptáme se na něj znovu) -> ukáže výsledek a znovu se ptá, pokud uživatel vloží nyní jako první operátor a pak číslo, tak kalkulačka spočte `předchozí výsledek, operátor, nové číslo` a ukáže výsledek. Takto lze opakovat do nekonečna. Program se ukončí pokud kdykoliv na vstup uživatel napíše 'q'.