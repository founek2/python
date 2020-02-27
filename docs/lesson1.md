# 1. Lekce
> Stolní pc:
>   * user: Guest
>   * password: Akademie19

## Co je python?
* skriptovací programovací jazyk
    * výchozí interpret CPython
* Vznikl 1991
* často využíván v OS Linux, Data science
* dobře čitelný - narozdíl od Javy C++ a jiných

## Jak ho zapnout?
V terminálu lze jednoduše vyvolat interpret příkazem: ```python3```.
Spustí se prostředí a nyní lze přímo psát python kód, kde po stisknutí klávesy enter se řádek vyhodnotí a zobrazí se jeho výstup (přesněji hodnota daného výrazu).

## Primitivní datové typy
* str - string, textová hodnota ```promnena = "nějaká hodnota"```
* bool -  ```promnena = True```
* int -  ```promnena = 123```
* flaot -  ```promnena = 0.981```

## Podmínky
```python
promena = 3
if promena > 4:                      # vyhodnotí se False
    print("promena je větší než 4")
elif promena < 1:                    # vyhodnotí se False
    print("promena je menší než 1")
else:                                # výchozí chování, pokud žádný if nebyl splněn
    print("promena je v rozsahu: 1 <= promnena <= 4")
```

## Volání funkce?
Každá funkce má nějaký název, pomocí kterého na ni lze odkázat. Při volání za jméno přidáme závorky. Tedy pokud chceme zavolat funkci pro výpis textu s názvem print, tak stačí `print()`. Takto ale funkce neví co má vypsat, takže je potřeba ji předat nějakou hodnotu. To lze udělat tak, že se jednotlivé hodnoty napíší do závorek. Pokud jich je více, tak se oddělují čárkou. Např. výpis slova "#strahov" -```print("#strahov")```. Jednotlivé hodnoty v závorkách se označují jako `parametry`.


## Základní vestavěné funkce (built-in)
* ```print()``` - parametry: co chci vypsat
* ```input()``` - parametr: text který se zobrazí uživateli
* ```range()``` - parametry: (od, do, krok) - do je exkluzivní, tedy range(1, 9) jsou čísla 1-8
* ```len()``` - parametr: textový řetězec (vrátí počet jeho znaků)


## Cičení
### 1.1.x Čísla
* Sečtěte čísla 1, 5 a 98
* Spočítejnte třetí mocninu čísla 11
* Spočítejnte kolikrát se vejde číslo 7 do 51
* Zjistěte zbytek po dělení 15 / 4  (nápověda: výsledek je celočíselný 0 <= x < 4) 

> CheatSheet pro matematické operátory:
> * `+` sčítání: 3 + 10 -> 13
> * `-` odčítání: 3 - 10 -> -7
> * `/` dělení: 9 / 2 -> 4.5
> * `//` celočíselné dělení (odsekne zbytek) 9 // 2 -> 4
> * `%` zbytek po dělení 9 % 2 -> 1
> * `**` umocní číslo před operátorem na číslo za operátorem 2 ** 3 -> 8

### Řetězce
U řetězcu se dá doptat na jednotlivé znaky pomocí pozice. Pozice vždy začíná na 0 a získat n-tý znak se dá takto:
```python
text = "Nice kitty"
text[0]     –> "N"
text[1]     –> "i"
text[2]     –> "c"
text[3]     –> "e"
text[4]     –> " "
.
.
.
text[9]     –> "y"
```
Dále funguje také dotazování na pozice od zadu (záporná adresace). Poslední znak získáme `text[-1]`, předposlední `text[-2]` atd.

### 1.2.{1-3} Řetězce
* Vypište počet znaků ve vašem jměné. Pro načtení jména použijte funkci ```input()```
* vypište 3. znak z vašeho jména
* vypište poslední znak z vašeho jména

> ### Řetězce formátování
> Jednotlivé řetězce jsou spojovat pomoci operátoru `+` nebo lze využít moderní přístup tzv. f-strings. Stačí před úvozovky řetězce dát písmeno `f` a v řetezci lze do závorek `{}` napsat promněnou, která si při zpracování nahradí svojí hodnotou.
> ```python
> game = 'Lineage II'
> 'Moje neoblíbenější pc hra je' + ' ' + game   # výstup -> "Moje neoblíbenější pc hra je Lineage II"
> f'Moje neoblíbenější pc hra je {game}'        # výstup -> "Moje neoblíbenější pc hra je Lineage II"
> ```

#### 1.2.4 Řetězce
Vypište následující text s použitím pouze jednoho volání funkce print, `jméno` a `počet` nepište do textu napřímo ale uložte si je do promněné a ty využijte pro výpis.
```python
Jmenuji se {vaše jméno} a na Strahově jsem již {počet} let
```

## Cykly
```python
for number in 0,1,2,3,4,5,6:
    print(number)   # vypíše všechna čísla od 1 do 9

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

### 1.3.x Cykly
* Vypište přesně 11x vaše jméno
* Sečtěte všechna čísla od 0 do 49
* vypište všechna lichá čísla z intervalu <7, 19>

### 1.4 Kalkulačka - zjednodušená
Vytvořte program, který se uživatele zeptá nejprve na jedno číslo, potom na druhé a nakonec na matematický operátor. Tyto 3 vstupy uložte do přemněných a pomocí podmínek otestujte jestli operátor je jeden z `+ - * /`, pokud ano, tak spočítejte hodnotu výrazu a zobrazte uživateli, pokud operátor není jeden z povolených, tak vypište nějaký text jako chybu a zavolejte funkci `exit` s parametrem 1 - funkce exit ukončí běh programu a číslo 1 signalizuje, že nastala chyba. 
