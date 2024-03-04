# 2. Lekce

## Proměnné II

* jmenná konvence - angličtina, popisné názvy
* snake case - např. `car_color`

## "Rozloučení" s interaktivním módem

Interpretr v interaktivním módu je užitečná věc, pokud si potřebujeme vyzkoušet 1 - 3 řádkové přikazy. Pokud ale chceme psát delší skripty nebo mít možnost se vracet do historie a opakovaně spouště více řádků, tak tento řežim je velmi nepraktický. Proto si ukážeme jak spustit skript, který je uložený v souboru. Ale nebojte, s interaktivním režimem se jistě ještě potkáme a velice ho doporučují, pokud si potřebujete vyzkoušet několiká málo řádkové příkazy - velmi se hodí. Jak vlastně spustit soubory s python kódem? (název souboru s kódem je muj_skript.py)

```bash
python3 muj_skript.py
```

## Cykly

```python
for number in 0,1,2,3,4,5,6:
    print(number)   # vypíše všechna čísla od 0 do 6

for number in range(7):
    if number == 2:
        print(number)   # vypíše poze číslo 2

for number in range(1, 10):
    if 2 <= number <= 8:    # specialita Pythonu
        print(number)   # vypíše číslo v rozmezí daném podmínkou
```

## Odsazení místo závorek

Z výše uvedené ukázky je viděť, že python nepoužívá závorky pro uvození bloku jako C jazyky, ale nad blokem je řádek končící dvojtečkou a pak každý rádek, který je odsazen patří do bloku. Blok končí prvním řádkem, který nemá dané odsazení. Je potřeba si na odsazení dávat pozor, protože rozdíl v jedné mezeře může vyvolat chybu. Bloky lze také libovolně vnořovat.

```python
for number in range(1, 10):             <- začátek bloku1
    print("Strahov je životní styl")
   _
   └───odsazení

    for number2 in range(1, 10):         <- nový vnořený blok2
        print(number)                   <- kód vnořeného bloku2
        print(number2)
    promnena = number + 1               <- uzavření bloku2 a kód pro blok1
    print("hodnota", promnena)
                                        <- uzavření bloku1
print("konec programu")                 <- globální kód
```

### 2.1.x Cykly

* Vypište přesně 11x vaše jméno
* Sečtěte všechna čísla od 0 do 49
* vypište všechna lichá čísla z intervalu <7, 19>

### 2.2 Kalkulačka - zjednodušená

Vytvořte program, který se uživatele zeptá nejprve na jedno číslo, matematický operátor a nakonec na druhé číslo. Tyto 3 vstupy uložte do přemněných a pomocí podmínek otestujte jestli operátor je jeden z `+ - * /`, pokud ano, tak spočítejte hodnotu výrazu a zobrazte ji uživateli. Pokud operátor není jeden z povolených, tak vypište nějaký text jako chybovou hlášku a zavolejte funkci `exit` s parametrem 1 - funkce exit ukončí běh programu a číslo 1 signalizuje, že nastala chyba.

[Referenční_řešení](_examples/calc_easy)

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

## Fce Range - parametry

Funkci range lze zavolat s různým počtem parametrů. Pokud dostane pouze jeden argument `n`, tak vrátí posloupnost začínající od 0 s n prvky -> tedy 0,1,2,...,n-1  
Pokud předáme parametry 2 např. `range(2, 10)`, tak návratová hodnotu bude posloupnost začínající číslem 2 a končí číslem 9 (parametr je exkluzivní) -> tedy 2,3,4,...,9  
Další možnost je předat parametry 3 např. `range(1, 10, 2)`. První parametr opět udává počátek posloupnosti a druhý exkluzivní maximální hodnotu, třetí parametr určuje krok. Tedy v našem případě výsledná posloupnost bude 1,3,5,7,9

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

### 2.3.x Cvičení na pole

* Vytvořte promněnou s prázdnám polem a vložte do něj prvky 100 až 199 (nedělejte to manuálně, ale použijte cyklus). Následně vypište každý třetí prvek z daného pole.
* Vytvořte list s alespoň 10 čísly a následně spočítejte průměr z hodnot

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

## Konstruktory primitivů

Není '3' (textový řetězec) stejné jako 3 (celé číslo)

* 3 / `int`
* 0\. / `float`
* `bool`
* `''` / `""` / `str()`
* `[]` / `list()`
* `,` / `tuple()`
