# Author: Émile
# Date: 2026-02-02
# But:
from functools import reduce
import operator

# Classe Erreur perso
class ChoixInvalideError(Exception):
    pass



def calcularice() -> None:
    """
    Fonction principale de la calculatrice
    """
    # Variables globales
    memories = { # Dictionnaire pour stocker les valeurs
        "M1": None,
        "M2": None,
        "M3": None,
        "M4": None,
        "M5": None
    }
    current_memory = "M1" # Memoire active par default
    resultat = None



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
    def operations_simple(choix:str) -> str:
        """Fonctions qui fait le calcul d'operations simple
        (+, -, *, /, **, %)

        Args:
            choix (str): Contient le choix de l'operation a faire

        Raises:
            ZeroDivisionError: si l'utilisateur tente la division par zero ou le modulo par zero
            ValueError: si l'utilisateur tente un operation qui n'existe pas

        Returns:
            str: une string formatter qui contient le resultat
        """

        # Contient toutes les operations supporter ainsi que leurs operateurs et leurs logiques
        dict_operations = {
                "1": ("+", lambda a, b: a + b),
                "2": ("-", lambda a,b: a - b),
                "3": ("*", lambda a,b: a * b),
                "4": ("/", lambda a,b: a / b),
                "5": ("**", lambda a,b: a ** b),
                "6": ("%", lambda a,b: a % b)
                }
        nonlocal resultat

        # verifie si le choix est dans les operations supporter
        if choix in dict_operations:
            num1 = utiliser_memoire_dans_calcul("Entrez le premier nombre : ")
            num2 = utiliser_memoire_dans_calcul("Entrez le deuxième nombre : ")

            operateur, operations = dict_operations[choix]

            if operateur in ["/", "%"] and num2 == 0:
                raise ZeroDivisionError(f"{'Division' if operateur == '/' else 'Modulo'} par zéro est impossible !")

            resultat = operations(num1, num2)

            return f"Résultat : {num1} {operateur} {num2} = {resultat}"
        else:
            raise ValueError("Choix invalide. Veuillez entrer une operation entre 1 et 6")

    # Operations multiples
    def operations_multiples() -> str:
        """Fonctions qui le calcul d'operations a plusieurs arguments

        Raises:
            ChoixInvalideError: si l'utilisateur tente une operation qui n'existe pas
            ValueError: option invalide
            ValueError: option invalide
            ZeroDivisionError: si l'utilisateur tente la division par zero ou le modulo par zero
            ValueError: option invalide

        Returns:
            str: une string formater qui contient le calcul et le resultat
        """
        nonlocal resultat

        print("\n=== MODE OPÉRATIONS MULTIPLES ===\n")

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
                choix_operations = input("Opération (+, -, *, /): ").strip()

                # valide le choix de loperation
                if choix_operations not in dict_operations:
                    raise ChoixInvalideError(f"({choix_operations}) - n'est pas une operations valide.")

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
                            input_nbr = utiliser_memoire_dans_calcul(f"Entrez le nombre {i+1}: ")

                            if (choix_operations == "/" or choix_operations == "%") and i >= 1:
                                if input_nbr == 0:
                                    raise ZeroDivisionError(f"{"Division" if choix_operations == "/" else "Modulo"} par zéro est impossible!")

                            lst_nbr.append(input_nbr)
                            break
                        except ValueError as ve:
                            raise ValueError("Veuillez entrer un nombre valide.")

                # effectue l'operation demander sur la liste de nombres recus
                resultat = dict_operations[choix_operations](lst_nbr)

                # formattage du calcul pour son affichage
                calcul = f" {choix_operations} ".join(str(nbr) for nbr in lst_nbr)
                return f"Calcul: {calcul} = {resultat}"



            except ChoixInvalideError as cive:
                print(f"Erreur: {cive}")

            except ValueError as ve:
                print(f"Erreur: {ve}")

    # fonctions de memoires
    def afficher_memoires(dispo_seulement=False) -> None:
        """Affiche toutes les memoires et leurs valeurs, a un toggle pour n'afficher que les memoires qui on une valeur

        Args:
            dispo_seulement (bool, optional): permet l'affichage des memoires qui on une valeurs seulement. Defaults to False.
        """
        for key in memories.keys():
            if dispo_seulement:
                if memories[key] != None:
                    print(f"{key}: {memories[key]}")
            else:
                print(f"{key}: {"vide" if memories[key] == None else memories[key]}")


    def stocker_resultat_en_memoire(): # stocke le resultat le plus recent en memoire
        """Stocke le resultat le plus recent (si il existe) dans la memoire active

        Raises:
            ValueError: si le resultat est vide
        """
        nonlocal resultat
        nonlocal current_memory

        try:
            # verifie si le resultat est vide
            if resultat == None:
                raise ValueError("Aucun resultat n'est disponible dans la memoire active")

            # si le resultat a une valeurs, update la memoire courante
            memories[current_memory] = resultat
            print(f"Résultat {resultat} stocké dans {current_memory}")

            # change la memoire active pour la prochaine memoire vide
            for key in memories.keys():
                if memories[key] == None:
                    current_memory = key
                    break

        except ValueError as ve:
            print(f"Erreur: {ve}")

    def utiliser_memoire_dans_calcul(fallback_question) -> float: # permet d'utiliser une memoire dans un calcul
        """Permet d'utiliser un resultat en memoire lors d'une operation. Ne peut etre utiliser que lors d'une operations

        Args:
            fallback_question (_type_): Question que devrait poser le input si l'utilisateur ne souahite pas utiliser de resultat en memoire

        Raises:
            ValueError: option invalide
            ValueError: option invalide

        Returns:
            flaot: retourne la memoire sous forme de float, sinon demande un float a l'utilisateur
        """
        while True:
            try:
                choix = input("Utiliser une mémoire ? (o/n)").strip().lower()

                if choix not in ['o', 'n']:
                    raise ValueError("Choix non valide.")

                if choix == 'o':
                    print("Memoire disponible:")
                    #affiche les memoires disponibles
                    afficher_memoires(True)

                    try:
                        choix_memoires = input("Choix: ").strip().capitalize()

                        if choix_memoires not in memories:
                            raise ValueError("La memoire choisie n'existe pas")

                        if memories[choix_memoires] != None:
                            return (memories[choix_memoires]) # type: ignore

                    except ValueError as ve:
                        print(f"Erreur: {ve}")

                if choix == "n":
                    return nombre_valide(fallback_question)
            except ValueError as ve:
                print(f"Erreur: {ve}")

    def effacer_memoire():
        """permet d'effacer les memoires

        Raises:
            ValueError: option invalide
            ValueError: option invalide
        """
        try:
            print("1. Effacer toutes les memoires.")
            print("2. Effacer une seule memoires")
            choix = input("Choix: ").strip()

            if choix not in ['1', '2']:
               raise ValueError("votre choix n'est pas valide")

            if choix == '1':
                for key in memories.keys():
                   memories[key] = None

                print("Supression de toutes les memoire effectuer.")
                afficher_memoires()

            if choix == '2':
                try:
                    print("Quelles memoires voulez vous supprimer:")
                    afficher_memoires()

                    choix_del = input("Choix: ")

                    if choix_del not in memories:
                        raise ValueError("la memoire selectionner n'est pas valide")

                    memories[choix_del] = None
                    print(f"Suprression de {choix_del} effectuer.")
                    afficher_memoires()

                except ValueError as ve:
                    print(f"Erreur: {ve}")


        except ValueError as ve:
            print(f"Erreur: {ve}")



    # Gestion de memoires
    def gestion_memoire():
        """Menu de gestion de memoire

        Raises:
            ValueError: option invalide
        """
        print(f"\n=== GESTION DE LA MÉMOIRE (Active: {current_memory}) ===\n")

        while True:
            print("a. Stocker le dernier résultat")
            print("b. Utiliser une mémoire dans un calcul")
            print("c. Afficher toutes les mémoires")
            print("d. Effacer une mémoire")
            print("e. Retour au menu principal")

            try:
                choix = input("Choix: ").strip()

                # validation du choix
                if choix not in ['a','b','c','d','e','q']:
                    raise ValueError(f"({choix}) - n'est pas une options valide")

                # retours au menu principal
                if choix == "e" or choix == "q":
                    break

                # Stocker le dernier resultat
                if choix == "a":
                    stocker_resultat_en_memoire()

                # utilisation d'une memoire dans un calcul
                if choix == "b":
                    print("Non disponible a cet endroit")

                # afficher toutes les memoires
                if choix == "c":
                    print("\nMémoires actuelles:")
                    afficher_memoires()
                    print()

                # effacer une ou toute les memoires
                if choix == "d":
                    effacer_memoire()

            except(ValueError) as ve:
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

            # Menu de gestion de memoire (8)
            if choix == "8":
                gestion_memoire()


        except ValueError as ve:
            print(f"Erreur: {ve}")
        except ZeroDivisionError as zde:
            print(f"Erreur: {zde}")
        except Exception as e:
            print(f"Erreur inattendue: {e}")


calcularice()
