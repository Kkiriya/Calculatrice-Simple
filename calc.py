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
        print("5. Modulo (%)")
        print("6. Puissance (**)")
        print("7. Quitter")

        try:
            choix = input("Quel est votre choix (1-6): ")

            if choix == '7':
                break;

            if choix not in ['1', '2', '3', '4', '5', '6']:
                raise ValueError("Choix invalide. Veuillez entrer un nombre entre 1 et 5")

            try:
                num1 = float(input("Entrez le premier nombre: "))
                num2 = float(input("Entrez le deuxieme nombre: "))

            except ValueError:
                raise ValueError("Veuillez entrez un nombre valide.")

            match(choix):
                case "1":
                    resultat = num1 + num2
                    ope = "+"

                case "2":
                    resultat = num1 - num2
                    ope = "-"

                case "3":
                    resultat = num1 * num2
                    ope = "*"

                case "4":
                    if num2 == '0':
                        raise ZeroDivisionError("Division par zero impossible!")

                    resultat = num1 / num2
                    ope = "/"

                case "5":
                    if num2 == '0':
                        raise ZeroDivisionError("Modulo par zero impossible!")
                    resultat = num1 % num2
                    ope = "%"

                case "6":
                    resultat = num1 ** num2
                    ope = "**"

            print(f"{num1} {ope} {num2} = {resultat}")
            exit_calc()


        except ValueError as ve:
            print(f"Erreur: {ve}")

        except ZeroDivisionError as zde:
            print(f"Erreur: {zde}")

        except Exception as e:
            print(f"Erreur inattendue: {e}")






calculatrice()
