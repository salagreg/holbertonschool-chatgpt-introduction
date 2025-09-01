#!/usr/bin/python3

import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_mines = mines
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_cells = width * height
        self.revealed_count = 0

    def print_board(self, reveal=False):
        clear_screen()
        # En-tête avec numéros de colonnes (sans préfixe)
        print(' '.join(str(i) for i in range(self.width)))

        for y in range(self.height):
            # Numéro de ligne seul sur sa ligne
            print(str(y))

            # Contenu de la ligne
            row_content = []
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        row_content.append('*')
                    else:
                        count = self.count_mines_nearby(x, y)
                        row_content.append(str(count) if count > 0 else ' ')
                else:
                    row_content.append('.')
            print(' '.join(row_content))

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Vérifier si les coordonnées sont valides
        if not (0 <= x < self.width and 0 <= y < self.height):
            return None  # Coordonnées invalides

        # Si la cellule est déjà révélée, ne rien faire
        if self.revealed[y][x]:
            return True

        # Si c'est une mine, le jeu se termine
        if (y * self.width + x) in self.mines:
            return False

        # Révéler la cellule
        self.revealed[y][x] = True
        self.revealed_count += 1

        # Si il n'y a pas de mines autour, révéler les cellules adjacentes
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < self.width and
                        0 <= ny < self.height and
                        not self.revealed[ny][nx]
                    ):
                        self.reveal(nx, ny)

        return True

    def check_win(self):
        """Vérifie si toutes les cellules non minées ont été révélées"""
        return self.revealed_count == (self.total_cells - self.total_mines)

    def play(self):
        while True:
            self.print_board()

            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                result = self.reveal(x, y)

                if result is None:
                    print("Invalid coordinates!")
                    continue
                elif result is False:
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                elif self.check_win():
                    self.print_board()
                    print("Congratulations! You've won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
