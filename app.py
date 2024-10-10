# Fonction pour afficher le plateau de jeu
def afficher_plateau(plateau):
    print("\n")
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 5)
    print("\n")

# Fonction pour vérifier s'il y a un gagnant
def verifier_victoire(plateau, joueur):
    # Vérifier les lignes
    for ligne in plateau:
        if ligne.count(joueur) == 3:
            return True
    # Vérifier les colonnes
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] == joueur:
            return True
    # Vérifier les diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur or \
       plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
        return True
    return False

# Fonction pour vérifier si le plateau est plein
def est_plein(plateau):
    for ligne in plateau:
        if " " in ligne:
            return False
    return True

# Fonction principale du jeu
def jouer_morpion():
    # Initialiser le plateau vide
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    
    joueur_actuel = "X"
    jeu_en_cours = True

    print("Bienvenue dans le jeu de Morpion !")
    afficher_plateau(plateau)

    while jeu_en_cours:
        # Demander au joueur de saisir la position
        try:
            position = int(input(f"Joueur {joueur_actuel}, entrez un nombre (1-9) pour placer votre symbole: "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")
            continue
        
        # Calculer les coordonnées de la position
        if position < 1 or position > 9:
            print("Position invalide. Choisissez un nombre entre 1 et 9.")
            continue
        ligne = (position - 1) // 3
        col = (position - 1) % 3

        # Vérifier si la case est déjà occupée
        if plateau[ligne][col] != " ":
            print("Cette case est déjà prise. Essayez à nouveau.")
            continue
        
        # Placer le symbole sur le plateau
        plateau[ligne][col] = joueur_actuel
        afficher_plateau(plateau)

        # Vérifier s'il y a un gagnant
        if verifier_victoire(plateau, joueur_actuel):
            print(f"Félicitations ! Le joueur {joueur_actuel} a gagné !")
            jeu_en_cours = False
        elif est_plein(plateau):
            print("Match nul ! Le plateau est plein.")
            jeu_en_cours = False
        else:
            # Changer de joueur
            joueur_actuel = "O" if joueur_actuel == "X" else "X"

if __name__ == "__main__":
    jouer_morpion()
