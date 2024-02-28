import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.configure(background="#ffffff")  # Color de fondo blanco
        
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_widgets()
        
        self.root.mainloop()
        
    def create_widgets(self):
        # Botones
        new_game_button = tk.Button(self.root, text="Nuevo Juego", command=self.new_game, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        new_game_button.grid(row=0, column=0, padx=5, pady=5)
        
        choose_token_button = tk.Button(self.root, text="Escoger Token", command=self.choose_token, bg="#FFC107", fg="white", font=("Arial", 12, "bold"))
        choose_token_button.grid(row=0, column=1, padx=5, pady=5)
        
        creator_button = tk.Button(self.root, text="Creador: Tú", command=self.show_creator, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        creator_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Tablero
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', width=8, height=4, command=lambda row=i, col=j: self.play(row, col), bg="#BDBDBD", font=("Arial", 24, "bold"))
                self.buttons[i][j].grid(row=i+1, column=j, padx=5, pady=5)
                
    def new_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j]['text'] = ''
        self.current_player = 'X'
        
    def choose_token(self):
        pass  # Aquí podrías implementar la lógica para que el jugador elija su token
    
    def show_creator(self):
        messagebox.showinfo("Creador", "Este juego fue creado por ti")
        
    def play(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner():
                messagebox.showinfo("¡Fin del Juego!", f"Ganador: {self.current_player}")
                self.new_game()
            elif self.check_draw():
                messagebox.showinfo("¡Fin del Juego!", "Empate")
                self.new_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            messagebox.showwarning("Movimiento inválido", "Esta casilla ya está ocupada")
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

if __name__ == "__main__":
    TicTacToe()
