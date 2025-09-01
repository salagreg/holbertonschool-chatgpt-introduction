#!/usr/bin/python3


def print_board(board):
    """Affiche le plateau de jeu"""
    print("\nPlateau actuel:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print()


def check_winner(board):
    """Vérifie s'il y a un gagnant"""
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if (
            board[0][col] == board[1][col] == board[2][col]
            and board[0][col] != " "
        ):
            return True

    if (
        board[0][0] == board[1][1] == board[2][2]
        and board[0][0] != " "
    ):
        return True
    if (
        board[0][2] == board[1][1] == board[2][0]
        and board[0][2] != " "
    ):
        return True

    return False


def check_board_full(board):
    """Vérifie si le plateau est plein (match nul)"""
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_input(prompt, valid_range):
    """
    Obtient une entrée valide utilisateur avec gestion complète des erreurs

    Parameters:
        prompt (str): le texte affiché à l'utilisateur.
        valid_range (list): les valeurs acceptées.

    Returns:
        int: la valeur choisie.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Erreur: Veuillez entrer une valeur.")
                continue
            value = int(user_input)
            if value not in valid_range:
                print(
                    f"Err: nbr entre {min(valid_range)} & {max(valid_range)}."
                )
                continue
            return value
        except ValueError:
            print("Erreur: Veuillez entrer un nombre entier valide.")
        except KeyboardInterrupt:
            print("\nJeu interrompu par l'utilisateur. Au revoir!")
            exit()
        except EOFError:
            print("\nFin d'entrée détectée. Au revoir!")
            exit()


def get_player_move(player):
    """
    Obtient le coup d'un joueur avec validation complète

    Parameters:
        player (str): 'X' ou 'O'.

    Returns:
        tuple: (ligne, colonne)
    """
    print(f"Tour du joueur {player}")
    try:
        row = get_valid_input(
            f"Entrez la ligne (0, 1, ou 2) pour le joueur {player}: ",
            [0, 1, 2]
        )
        col = get_valid_input(
            f"Entrez la colonne (0, 1, ou 2) pour le joueur {player}: ",
            [0, 1, 2]
        )
        return row, col
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return get_player_move(player)


def tic_tac_toe():
    """Fonction principale du jeu Tic-Tac-Toe"""
    print("=== Bienvenue au Tic-Tac-Toe ===")
    print("Instructions:")
    print("- Entrez les coordonnées de 0 à 2 pour les lignes et colonnes")
    print("- Le joueur X commence")
    print("- Pour quitter, utilisez Ctrl+C")

    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    move_count = 0

    try:
        while True:
            print_board(board)

            if check_winner(board):
                winner = "O" if player == "X" else "X"
                print(f"🎉 Félicitations! Le joueur {winner} a gagné! 🎉")
                break

            if check_board_full(board):
                print("🤝 Match nul! Le plateau est plein. 🤝")
                break

            row, col = get_player_move(player)

            if board[row][col] == " ":
                board[row][col] = player
                move_count += 1
                player = "O" if player == "X" else "X"
            else:
                print("❌ Cette case est déjà occupée! Essayez une autre case.")
                continue

    except KeyboardInterrupt:
        print("\n🚪 Jeu interrompu. Au revoir!")
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        print("Le jeu se termine.")

    print(f"\nNombre total de coups joués: {move_count}")
    print("Merci d'avoir joué au Tic-Tac-Toe!")


def main():
    """Point d'entrée principal avec option de rejouer"""
    while True:
        try:
            tic_tac_toe()
            while True:
                try:
                    replay = input(
                        "\nVoulez-vous jouer une nouvelle partie? (o/n): "
                    ).strip().lower()
                    if replay in ['o', 'oui', 'y', 'yes']:
                        break
                    elif replay in ['n', 'non', 'no']:
                        print("Au revoir et merci d'avoir joué!")
                        return
                    else:
                        print("Veuillez répondre par 'o' (oui) ou 'n' (non).")
                except KeyboardInterrupt:
                    print("\nAu revoir!")
                    return
        except KeyboardInterrupt:
            print("\nAu revoir!")
            break
        except Exception as e:
            print(f"Erreur fatale: {e}")
            break


if __name__ == "__main__":
    main()
