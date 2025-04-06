import random

# 1.1 ComplexModel1: Diszlexiás

# Véletlenszerű elem kiválasztása
def uniform_draw(options):
    return random.choice(options)

def complex_model_1():
    # Lehetséges jellemzõk
    feature1 = ['könyvtáros', 'tanár']
    feature2 = ['csendes', 'cserfes']
    operator = [' és ', ' vagy ']
    
    # következtetés véletlenszerű generálása
    word1 = uniform_draw(feature1)  # Panni foglalkozása
    op = uniform_draw(operator)  # Logikai kapcsolat (és/vagy)
    word2 = uniform_draw(feature2)  # Panni tulajdonsága
    
    print(f'Premissza: Panni {word1}{op}{word2}.')
    
    # bizonyos valószínűséggel felcseréli a csendes/cserfes szavakat
    if random.random() < 0.3:  # 30% eséllyel eltéveszti a tulajdonságot
        possible_mistakes = [w for w in feature2 if w != word2]  # Rossz változatok keresése
        word3 = uniform_draw(possible_mistakes)  # Véletlenszerűen kiválaszt egy hibás szót
    else:
        word3 = word2  # Ha nem téveszt, az eredeti marad
    
    print(f'Konklúzió: Panni {word3}.')
    
    # ellenõrzi hogy érvényes-e
    ervenyes = 'nem érvényes'
    if op == ' és ' and word2 == word3:  # "és" csak akkor érvényes, ha mindkét állítás igaz
        ervenyes = 'érvényes'
    
    print(ervenyes)
    return ervenyes

# 1.2 ComplexModel2: A logikai "és" 95%-ban helyes de 80%-ban a "vagy"-ot félreolvassa "és"-nek

def complex_model_2():
    # lehetséges jellemzõk
    feature1 = ['könyvtáros', 'tanár']
    feature2 = ['csendes', 'cserfes']
    operator = [' és ', ' vagy ']
    
    # következtetés generálása
    word1 = uniform_draw(feature1)
    op = uniform_draw(operator)
    word2 = uniform_draw(feature2)
    
    print(f'Premissza: Panni {word1}{op}{word2}.')
    
    # 95%-ban az "és" korrektül működik, de 80%-ban a "vagy"-ot "és"-nek értelmezi
    if op == ' és ':
        correct_logic = random.random() < 0.95  # 95%-os pontosság
    else:
        correct_logic = random.random() >= 0.8  # 80%-ban félreértelmezi "és"-ként
    
    # Következtetés generálása
    if correct_logic:
        word3 = word2  # Helyesen következtet
    else:
        word3 = uniform_draw(feature2)  # Véletlenszerű hibás következtetés
    
    print(f'Konklúzió: Panni {word3}.')
    
    # ellenõrzi hogy érvényes-e
    ervenyes = 'nem érvényes'
    if op == ' és ' and word2 == word3:
        ervenyes = 'érvényes'
    
    print(ervenyes)
    return ervenyes

# Teszteljük
for _ in range(5):
    print("--- ComplexModel1 ---")
    complex_model_1()
    print("--- ComplexModel2 ---")
    complex_model_2()
import itertools

# 1.3 2 kockadobás összege legalább 4
# összes lehetséges dobáspár
dobasok = list(itertools.product(range(1, 7), repeat=2))

# kiszûrjük ahol az összeg legalább 4
legalabb_4 = [dobas for dobas in dobasok if sum(dobas) >= 4]

# Valószínűség: kedvező / összes eset
valoszinuseg = len(legalabb_4) / len(dobasok)

print(f"A valószínűsége annak, hogy az összeg legalább 4: {valoszinuseg:.3f}")

import itertools

# francia kártya figurás lapjainak listája
szinek = ['kőr', 'treff', 'káró', 'pikk']
figurak = ['bubi', 'dáma', 'király', 'ász']

# összes figurás lap
kartyak = list(itertools.product(szinek, figurak))

# Feltétel ellenőrzés (A: az egyik lap nem kőr vagy a másik lap nem király)
def megfelel_e_kardfeltetel(huzas1, huzas2):
    szin1, figura1 = huzas1
    szin2, figura2 = huzas2
    
    # Az egyik lap nem kőr vagy a másik lap nem király
    return not ((szin1 == 'kőr' and figura2 == 'király') or (szin2 == 'kőr' and figura1 == 'király'))

# Generáljuk az összes lehetséges lapkiválasztást két lapot húzva visszatevés nélkül
eloszlas = []
for huzas1, huzas2 in itertools.combinations(kartyak, 2):
    if megfelel_e_kardfeltetel(huzas1, huzas2):
        eloszlas.append((huzas1, huzas2))

# Nézzük meg az eloszlást
print(f"Lehetséges események száma: {len(eloszlas)}")
print("Lehetséges események:", eloszlas)


# 3.1 2 lapból az egyik király, a másik nem 
from math import comb

# Összes 2 lapos húzás
ossz_huzas = comb(52, 2)

# Kedvező esetek: 1 király és 1 nem király, két sorrendben
kedvezo = 4 * 48 * 2

valoszinuseg = kedvezo / ossz_huzas
print(f"3.1 Valószínűség (egyik király, másik nem): {valoszinuseg:.4f}")


# 3.2 Feltételes eloszlás: P(X=x | X+Y+Z=7)
from collections import Counter

osszes = []
for x in range(4):
    for y in range(4):
        for z in range(4):
            if x + y + z == 7:
                osszes.append(x)

gyakorisag = Counter(osszes)
total = sum(gyakorisag.values())
print("\n3.2 Eloszlás P(X=x | X+Y+Z=7):")
for x in range(4):
    p = gyakorisag[x] / total
    print(f"P(X={x} | W=7) = {p:.4f}")


# 3.3 Monty Hall paradoxon szimuláció
import random

def monty_hall(valt):
    nyer = 0
    for _ in range(100000):
        autó = random.randint(0, 2)
        valasztas = random.randint(0, 2)
        lehetosegek = [i for i in range(3) if i != valasztas and i != autó]
        monty = random.choice(lehetosegek)
        if valt:
            valasztas = next(i for i in range(3) if i != valasztas and i != monty)
        if valasztas == autó:
            nyer += 1
    return nyer / 100000

print("\n3.3 Monty Hall szimuláció:")
print("Ha váltunk:", monty_hall(True))
print("Ha maradunk:", monty_hall(False))


# 3.4 Monty Hall beépített emberrel (50% pontosság)
def monty_insider(valt):
    nyer = 0
    for _ in range(100000):
        auto = random.randint(0, 2)
        insider_helyes = random.random() < 0.5
        tipp = auto if insider_helyes else random.randint(0, 2)
        valasztas = tipp

        lehetosegek = [i for i in range(3) if i != valasztas and i != auto]
        monty = random.choice(lehetosegek)

        if valt:
            valasztas = next(i for i in range(3) if i != valasztas and i != monty)

        if valasztas == auto:
            nyer += 1
    return nyer / 100000

print("\n3.4 Monty Hall (beépített ember, 50%):")
print("Ha váltunk:", monty_insider(True))
print("Ha maradunk:", monty_insider(False))


#4.1a Marginális eloszlás (P(X))
# P(X) kiszámítása az X változó értékeihez tartozó összes valószínűség összeadásával
def marginals(eloszlas):
    # X = szín (kártya 1 színe)
    szinek_count = {szin: 0 for szin in szinek}
    
    # Iterálunk az eloszláson, és összesítjük a színek előfordulását
    for huzas1, huzas2 in eloszlas:
        szin1, _ = huzas1
        szin2, _ = huzas2
        szinek_count[szin1] += 1
        szinek_count[szin2] += 1
    
    # Eloszlás számítása
    total_events = len(eloszlas)
    for szin in szinek_count:
        szinek_count[szin] /= total_events
        
    return szinek_count

# marginális eloszlás
szinek_marginalis = marginals(eloszlas)

# Eredmények
print("\nMarginális eloszlás (P(X)):")
for szin, prob in szinek_marginalis.items():
    print(f"P(X = {szin}): {prob:.3f}")

# 4.1 b rész
# Definiáljuk az eseményeket
# X = treff király vagy treff ász
# Y = pikk dáma

# Y = pikk dáma valószínűség
p_y = 0
for lap in lapok:
    szin, figura = lap
    if szin == 4 and figura == 2:  # pikk dáma
        p_y += 1

# X = treff király vagy treff ász
p_x_and_y = 0
for huzas in osszes_huzas:
    lap1, lap2 = huzas
    szin1, figura1 = lap1
    szin2, figura2 = lap2
    # az egyik treff király/ász, a másik pikk dáma
    if ((szin1 == 3 and figura1 == 2) or (szin1 == 3 and figura1 == 1)) and (szin2 == 4 and figura2 == 2):
        p_x_and_y += 1
    elif ((szin2 == 3 and figura2 == 2) or (szin2 == 3 and figura2 == 1)) and (szin1 == 4 and figura1 == 2):
        p_x_and_y += 1

# feltételes valószínűség
p_x_given_y = p_x_and_y / p_y

# a feltételes valószínűséget
print(f"P(X = treff király vagy treff ász | Y = pikk dáma) = {p_x_given_y}")

#4.2 hörcsög súlya

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# lexikonbeli prior (előzetes)
prior_mu = 32       # gramm
prior_sigma = 10    # gramm (nagy szórás, kevés információ)

# Megfigyelt adatok (mérések)
data = np.array([28, 31, 44, 29])
n = len(data)
data_mean = np.mean(data)
likelihood_sigma = 1  # feltételezett mérési hiba (szórás)

# Bayes frissítés (konjugált normál prior és likelihood)
posterior_sigma_sq = 1 / (n / likelihood_sigma**2 + 1 / prior_sigma**2)
posterior_sigma = np.sqrt(posterior_sigma_sq)

posterior_mu = posterior_sigma_sq * (
    data_mean * n / likelihood_sigma**2 + prior_mu / prior_sigma**2
)

# rajzolás
x = np.linspace(20, 45, 500)
prior_pdf = norm.pdf(x, prior_mu, prior_sigma)
posterior_pdf = norm.pdf(x, posterior_mu, posterior_sigma)

plt.plot(x, prior_pdf, label='Prior (N(32, 10))', linestyle='--')
plt.plot(x, posterior_pdf, label=f'Posterior (μ ≈ {posterior_mu:.2f}, σ ≈ {posterior_sigma:.2f})', color='darkblue')
plt.axvline(data_mean, color='gray', linestyle=':', label=f'Minták átlaga ({data_mean:.2f} g)')
plt.title('Hörcsög súlyának eloszlása - Bayes-frissítés után')
plt.xlabel('Súly (g)')
plt.ylabel('Valószínűség')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
