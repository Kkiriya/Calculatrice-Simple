# Author: Émile
# Date: 2026-01-29
# But: Créer une calculatrice simple en Python avec une gestion robuste des erreurs à l'aide des exceptions.
import sys

def choisir_nbr():
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
            break
        except(ValueError):
            print(f"Erreur: {nbr2} n'est pas un nombre!")

    return nbr1, nbr2

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
    print("=== CALCULATRICE SIMPLE ===")

    while True:
        # Afficher le menu
        print("\nOpérations disponibles :")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Quitter")

        str_choix = input("Votre choix (1-5): ")
        str_choix_valide = "12345"

        match(str_choix):
            case "1":
                nbr1, nbr2 = choisir_nbr()
                resultat = nbr1 + nbr2
                print(f"{nbr1} + {nbr2} = {resultat}")

                exit_calc()

            case "2":
                nbr1, nbr2 = choisir_nbr()
                resultat = nbr1 - nbr2
                print(f"{nbr1} - {nbr2} = {resultat}")

                exit_calc()

            case "3":
                nbr1, nbr2 = choisir_nbr()
                resultat = nbr1 * nbr2
                print(f"{nbr1} * {nbr2} = {resultat}")

                exit_calc()

            case "4":
                while True:
                    nbr1, nbr2 = choisir_nbr()
                    if nbr2 == 0:
                        print("Erreur: division par zero impossible")
                    else:
                        break

                resultat = nbr1 / nbr2
                print(f"{nbr1} / {nbr2} = {resultat}")

                exit_calc()

            case "5" | "q" | "Q":
                break

            case _:
                print(f"Erreur: {str_choix} n'est pas une option valide!")



calculatrice()
