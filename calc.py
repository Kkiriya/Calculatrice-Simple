# Author: Émile
# Date: 2026-01-29
# But: Créer une calculatrice simple en Python avec une gestion robuste des erreurs à l'aide des exceptions.
import sys
import operator

def choisir_nbr(op_w_err=()):
    while True:
        nbr1 = input("Nombre 1: ")
        try:
            nbr1 = float(nbr1)
            break
        except(ValueError):
            print(f"Erreur: {nbr1} n'est pas un nombre!")

    while True:
        nbr2 = input("Nombre 2: ")
        try:
            nbr2 = float(nbr2)
            if nbr2 == 0:
                print(f"Erreur: division/modulo par zero impossible!")
                continue
            else:
                break
        except(ValueError):
            print(f"Erreur: {nbr2} n'est pas un nombre!")

    return nbr1, nbr2

def operation(op,a, b):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "%": operator.mod,
        "**": operator.pow
    }
    return operators[op](a,b)

def exit_calc():
    while True:
        choix = input("Voulez vous continuer vos calcul ou quittez? (o/n): ").lower()
        if choix == "o":
            break

        elif choix == "n":
            sys.exit(0)

        else:
            print(f"Erreur: {choix} n'est pas une option valide!")


def calculatrice():
    """
    Fonction principale de la calculatrice
    """
    operations_supporter = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "%",
        "6": "**"
    }


    print("=== CALCULATRICE SIMPLE ===")

    while True:
        # Afficher le menu
        print("\nOpérations disponibles :")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("6. Puissance (**)")
        print("7. Quitter")

        choix = input("Votre choix (1-5): ")
        op_w_err = ("4", "5")

        if choix in choix_operations:
            nbr1, nbr2 = choisir_nbr(choix, op_w_err)
            print("")




calculatrice()
