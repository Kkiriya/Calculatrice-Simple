# Author: Émile
# Date: 2026-02-02
# But:
from functools import reduce
import operator

# Classe Erreur perso

class ChoixInvalideError(Exception):
    pass



def calcularice():
    """
    Fonction principale de la calculatrice
    """
    # Variables globales
    resultat = None
    operateur = None



    # Fonctions internes

    # Validation des nombres
    def nombre_valide(question_inp:str="Nombre: ") -> float:
        """Demande un nombre et le valide a l'utilisateur, puis le retourne sous float

        Args:
            question_inp (str, optional): Contient une question personnaliser a passer au input. Defaults to "Nombre: ".

        Raises:
            ValueError: raise une erreur si le nombre n'est pas un float

        Returns:
            float: retourne le nombre sous float
        """
        try:
            return float(input(question_inp))
        except ValueError:
            raise ValueError("Veuillez entrer un nombre valide.")

    # Operations simples
    def operations_simple(choix):
        # Contient toutes les operations supporter ainsi que leurs operateurs et leurs logiques
        dict_operations = {
                "1": ("+", lambda a, b: a + b),
                "2": ("-", lambda a,b: a - b),
                "3": ("*", lambda a,b: a * b),
                "4": ("/", lambda a,b: a / b),
                "5": ("**", lambda a,b: a ** b),
                "6": ("%", lambda a,b: a % b)
                }

        # verifie si le choix est dans les operations supporter
        if choix in dict_operations:
            num1 = nombre_valide("Entrez le premier nombre : ")
            num2 = nombre_valide("Entrez le deuxième nombre : ")

            operateur, operations = dict_operations[choix]

            if operateur in ["/", "%"] and num2 == 0:
                raise ZeroDivisionError(f"{"Division" if operateur == "/" else "Modulo"} par zéro est impossible !")

            resultat = operations(num1, num2)

            return f"Résultat : {num1} {operateur} {num2} = {resultat}"
        else:
            raise ValueError("Choix invalide. Veuillez entrer une operation entre 1 et 6")

    # Operations multiples
    def operations_multiples():
        print("=== MODE OPÉRATIONS MULTIPLES ===")

        # fonctions pour les cas specifique
        def chain_power(lst): # permet le calcul recursif de plusieurs exposant
            if len(lst) == 1:
                return lst[0]
            return lst[0] ** chain_power(lst[1:])

        # Contient toutes les operations supporter ainsi que leurs operateurs et leurs logiques
        dict_operations = {
            "+": lambda lst: reduce(operator.add, lst),
            "-": lambda lst: reduce(operator.sub, lst),
            "*": lambda lst: reduce(operator.mul, lst),
            "/": lambda lst: reduce(operator.truediv, lst),
            "**": lambda lst: chain_power(lst),
            "%": lambda lst: reduce(operator.mod, lst),
        }

        while True:
            try:
                choix_opertations = input("Opération (+, -, *, /): ").strip()

                # valide le choix de loperation
                if choix_opertations not in dict_operations:
                    raise ChoixInvalideError(f"({choix_opertations}) - n'est pas une operations valide.")

                # valide le nombre d'operation a effectuer de suite
                try:
                    choix_nbr_operations = int(input("Combien de nombres voulez-vous additionner?: ").strip())
                except:
                    raise ValueError("Veuillez entrer un nombre valide.")

                if choix_nbr_operations < 2:
                    raise ValueError("Le nombre d'operations doit etre plus grand ou egale a 2")

                # demande les nombres sur lequel il faut effectuer loperation
                lst_nbr = []

                for i in range(choix_nbr_operations):
                    # le while permet de verifier les erreurs de manieres plus interactive
                    while True:
                        try:
                            input_nbr = float(input(f"Entrez le nombre {i+1}: "))

                            if (choix_opertations == "/" or choix_opertations == "%") and i >= 1:
                                if input_nbr == 0:
                                    raise ZeroDivisionError(f"{"Division" if choix_opertations == "/" else "Modulo"} par zéro est impossible!")

                            lst_nbr.append(input_nbr)
                            break
                        except ValueError as ve:
                            raise ValueError("Veuillez entrer un nombre valide.")

                # effectue l'operation demander sur la liste de nombres recus
                resultat = dict_operations[choix_opertations](lst_nbr)

                # formattage du calcul pour son affichage
                calcul = f" {choix_opertations} ".join(str(nbr) for nbr in lst_nbr)
                return f"Calcul: {calcul} = {resultat}"



            except ChoixInvalideError as cive:
                print(f"Erreur: {cive}")

            except ValueError as ve:
                print(f"Erreur: {ve}")






    print("=== CALCULATRICE SIMPLE ===")

    while True:
        # Afficher le menu
        print("\nOpérations disponibles :")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Puissance (**)")
        print("6. Modulo(%)")
        print("7. Opertatons multiples (plus de 2 nombres)")
        print("8. Gestion de la memoire")
        print("9. Quitter")

        try:
            choix = input("Quel est votre choix (1-9): ").strip()

            # Validation des choix
            if choix not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "m"]:
                raise ValueError("Choix invalide. Veuillez entrer un nombre entre 1 et 9")
                continue

            # Quitter (9 ou q)
            if choix == "9" or choix == "q":
                print("Merci d'avoir utilisé la calculatrice. Au revoir !")
                break

            # Operations Simple (1 - 6)
            if choix in ["1", "2", "3", "4","5","6"]:
                print(operations_simple(choix))
                continue

            # Operations multiples (7)
            if choix == "7":
                print(operations_multiples())
                continue


        except ValueError as ve:
            print(f"Erreur: {ve}")
        except ZeroDivisionError as zde:
            print(f"Erreur: {zde}")
        except Exception as e:
            print(f"Erreur inattendue: {e}")


calcularice()
