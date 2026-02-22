# Fougère de Barnsley

Génération et affichage de la [fougère de Barnsley](https://fr.wikipedia.org/wiki/Foug%C3%A8re_de_Barnsley), une fractale créée par le mathématicien Michael Barnsley. Le programme utilise un système de fonctions itérées (IFS) pour produire une forme qui ressemble à une fougère naturelle.

## Principe

Quatre transformations affines sont appliquées de manière aléatoire à un point initial, chacune avec une probabilité différente :

| Transformation | Probabilité | Rôle |
|---|---|---|
| f1 | 1 % | Tige (base) |
| f2 | 85 % | Folioles successives (corps principal) |
| f3 | 7 % | Branche gauche |
| f4 | 7 % | Branche droite |

Après 100 000 itérations, les points tracés forment la fougère.

## Prérequis

- Python 3
- matplotlib

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install matplotlib
```

## Exécution

```bash
source .venv/bin/activate
python barnsley_fern.py
```

Une fenêtre s'ouvre et affiche la fougère fractale.
