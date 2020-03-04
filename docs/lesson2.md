# 2. Lekce

## Proměnné II
* jmenná konvence - angličtina, popisné názvy
* snake case - např. `car_color`

## "Rozloučení" s interaktivním módem
Interpretr v interaktivním módu je užitečná věc, pokud si potřebujeme vyzkoušet 1 - 3 řádkové přikazy. Pokud ale chceme psát delší skripty nebo mít možnost se vracet do historie a opakovaně spouště více řádků, tak tento řežim je velmi nepraktický. Proto si ukážeme jak spustit skript, který je uložený v souboru. Ale nebojte, s interaktivním režimem se jistě ještě potkáme a velice ho doporučují, pokud si potřebujete vyzkoušet několiká málo řádkové příkazy - velmi se hodí. Jak vlastně spustit soubory s python kódem? (název souboru s kódem je muj_skript.py)
```bash
python3 muj_skript.py
```


### 1.4 Kalkulačka - zjednodušená
Vytvořte program, který se uživatele zeptá nejprve na jedno číslo, matematický operátor a nakonec na druhé číslo. Tyto 3 vstupy uložte do přemněných a pomocí podmínek otestujte jestli operátor je jeden z `+ - * /`, pokud ano, tak spočítejte hodnotu výrazu a zobrazte ji uživateli. Pokud operátor není jeden z povolených, tak vypište nějaký text jako chybovou hlášku a zavolejte funkci `exit` s parametrem 1 - funkce exit ukončí běh programu a číslo 1 signalizuje, že nastala chyba. 

## Komentáře v kóde
```python
# tento blok dělá nějaký
# magic
if 99 < 10 and 30 > 1:
    ...

"""
Víceřádkový dokumentační
řetězec - primárně pro komentáře funkcí/objektů
"""
```

## Konstruktory primitivů
Není '3' (textový řetězec) stejné jako 3 (celé číslo)
* 3 / `int`
* 0\. / `float`
* `bool`
* `''` / `""` / `str()`
* `[]` / `list()`
* `,` / `tuple()`


## Fce Range - parametry
Funkci range lze zavolat s různým počtem parametrů. Pokud dostane pouze jeden argument `n`, tak vrátí posloupnost začínající od 0 s n prvky -> tedy 0,1,2,...,n-1  
Pokud předáme parametry 2 např. `range(2, 10)`, tak návratová hodnotu bude posloupnost začínající číslem 2 s 10 prvky -> tedy 2,3,4,...,9  
Další možnost je předat parametry 3 např. `range(1, 10, 2)`. První parametr opět udává počátek posloupnosti a druhý počet prvků, třetí parametr určuje krok. Tedy v našem případě výsledná posloupnost bude 1,3,5,7,9

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
* Vytvořte list s alespoň 10 čísly a následně spočítejte průměr z hodnot

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

### 2.3.x Cvičení funkce
* napište funkci `add`, která vezme dva argumenty a vrátí jejich součet
```add(4, 6) -> 10```
* napište funkci `show` která vypíše obsah listu do výstupu, který dostane jako parametr
```python
numbers = [1, 2, 4]
show(numbers) # -> nic nemusí vracet
```

### 2.3.3 Výpočet součtu
Napište program, který se uživatele bude dokola ptát na číslo. Toto číslo budete přičítat k dosavadnímu celkovému součtu předchozích čísel. (Využijte předchozí funkci add, kterou jste si napsali)

# Pravděpodobně až 3. lekce

## Str - split
Na každý řetězec lze zavolat metodu split, která nám umožňuje rozdělit řetězec na víc částí. Jako parametr se udává oddělovač, který split bude hledat v řetězci a v daném místě provede rozdělení. Návratová hodnota je List obsahující jednotlivé části.
```python
text = 'Příliš žluťoučký kůň úpěl ďábelské ódy'
text.split(' ')     # -> ['Příliš', 'žluťoučký', 'kůň', 'úpěl', 'ďábelské', 'ódy']
```

### 2.3.4 Statistika listu
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

## While cyklus
```python
i = 0
while i < 10:
    ... # some magic

    print(i)
    i += 1

for i in range(10):
    ...

    print(i)

# Výstup obou cyklů bude identický - vypíší čísla od 0 až do 9
```
Cyklus while se nejčastěji využívá pokud předem nevíme kolikrát budeme potřebovat kód zopakovat. Můžeme v průběhu měnit hodnotu řídící promněné - snižovat/zvyšovat. Díky tomu získáme cyklus s promněnou délkou opakování. Další časté využití:
```python
running = True
while running:
    ... # some magic

    if promnena == 3:
        running = False
```

<!-- Nejprve napsat vše do cyklu, potom vylepšit separací kódu do funkce-->
### 2.3.5 Kalkulačka podruhé
Program se zeptá na číslo, operátor, číslo -> ověří že čísla jsou čísla a operátor je známý operátor (pokud operátor neznáme, tak vypíšeme hlášku "neznámý operátor" a zeptáme se na něj znovu) -> ukáže výsledek a znovu se ptá, pokud uživatel vloží nyní jako první operátor a pak číslo, tak kalkulačka spočte `předchozí výsledek, operátor, nové číslo` a ukáže výsledek. Takto lze opakovat do nekonečna. Program se ukončí pokud kdykoliv na vstup uživatel napíše 'q'.
