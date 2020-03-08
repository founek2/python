# 3. Lekce

### 2.2.1 Kalkulačka - zjednodušená II
Využijte již naprogramovanou zjednodušenou kalkulačku, ale místo použití 3 promněných pro každou hodnotu, která se načítá od uživatele využijte list a cyklus. Stejně tak pro hlášky, které vypisujete uživateli.

## Funkce pokračování
V první lekci jsme si ukázali jak funkci zavolat, nyní si ukáže jak si můžeme vytvořit svoji vlastní. Používá se pro to klíčové slovo `def`, za kterým následuje název funkce a v závorkách názvy promněných do která se nám vloží parametry, pokud naší funkci někdo zavolá a nějaká parametry zadá.
```python
def kill_program(id, reasson):
    print(f'program with id: {id} was killed')
    print(f'Reason for kill: {reasson}')

    for i in range(15):
        ... # some black magic

    return True         # návratová hodnota

kill_program(2, 'I don`t like it')
```
Všimněte si slova `return` na konci funkce. Každá funkce může vracet nějakou hodnotu (stejně jako range nám vrací posloupnost), co vrátí je hodnota za slovem return. Příklad použtí:
```python
outcome = kill_program(1, 'Too high memory usage')

if outcome == True:
    print('Successfully killed')
else:
    print('Unable to kill')
```

### 3.1.x Cvičení funkce
* napište funkci `add`, která vezme dva argumenty a vrátí jejich součet
```add(4, 6) -> 10```
* Npište funkci is_bigger, která rozhodne jestli první argument (číslo) je větší než druhý (číslo) -> vrátí True pokud ano, jinak False
* napište funkci `show` která dostane jako parametr list a vypíše jeho obsah do konzole - list projděte pomocí for cyklu
```python
numbers = [1, 2, 4]
show(numbers) # -> nic nemusí vracet
```

### 3.1.3 Výpočet součtu
Napište program, který se uživatele bude dokola ptát na číslo. Toto číslo budete přičítat k dosavadnímu celkovému součtu předchozích čísel. (Využijte předchozí funkci `add`, kterou jste si napsali)

## Packing parameters
V pythonu lze napsat funkci, která bude přijímat libovolný počet argumentů. Lze toho dosáhnout pomocí "sbalení" parametrů do listu.
```python
def count(*params):
    return len(params)

count(1, 41, "Kitty", "SH", 0.1, False)     # -> 6

def count2(first, *others):
    return 1 + len(others)

count2(1, 41, "Kitty", "SH", 0.1, False)     # -> 6
```

## Str - split
Na každý řetězec lze zavolat metodu split, která nám umožňuje rozdělit řetězec na víc částí. Jako parametr se udává oddělovač, který split bude hledat v řetězci a v daném místě provede rozdělení. Návratová hodnota je List obsahující jednotlivé části.
```python
text = 'Příliš žluťoučký kůň úpěl ďábelské ódy'
text.split(' ')     # -> ['Příliš', 'žluťoučký', 'kůň', 'úpěl', 'ďábelské', 'ódy']
```

### 3.2.1 Statistika listu
Napište tyto 3 funkce:
* `inc` - parametr dostane list čísel a její úkol je přičíst ke každému číslu 1 a list vrátit
* `maxList` - parametr dostane list čísel a vrátí maximum
* `minList` - parametr dostane list čísel a vrátí minimum
* `sumList` - parametr dostane list čísel a vrátí součet
Vytvořte skript, který se zeptá uživatele na čísla oddělená čárkou. Načte vstup jako string, potom pomocí metody `split` převede na list a následně vypíše zajímavé statistiky v tomto formátu:
```text
min: {minimální prvek}
max: {maximální prvek}
sum: {součet}
inc: {list s hodnotami zvětšenými o 1}
orig: {list s původními hodnotami}
```
Použijte naivní řešení - cyklem projdete pole a v globální promněné budete mít minimum (analogicky max), které porovnánte se všemi prvky


<!-- Nejprve napsat vše do cyklu, potom vylepšit separací kódu do funkce-->
### 3.3.1 Kalkulačka podruhé
Program se zeptá na číslo, operátor, číslo -> ověří že čísla jsou čísla a operátor je známý operátor (pokud operátor neznáme, tak vypíšeme hlášku "neznámý operátor" a zeptáme se na něj znovu) -> ukáže výsledek a znovu se ptá, pokud uživatel vloží nyní jako první operátor a pak číslo, tak kalkulačka spočte `předchozí výsledek, operátor, nové číslo` a ukáže výsledek. Takto lze opakovat do nekonečna. Program se ukončí pokud kdykoliv na vstup uživatel napíše 'q'.


### Cvičení - TODO aplikace
Napište konzolovou aplikaci, která si bude udržovat v poli text úkolu a jeho stav (hotovo/vytvořeno). Uživateli nabídne jednoduché menu:
```
Menu: (pro výběr stiskněte danou klávesu)
Zobrazi vše - 'a'
Zobrazit hotové - 'd'
Zobrazit nové - 'n'
Přidat úkol - 'c'
Ukončit - 'q'
```

