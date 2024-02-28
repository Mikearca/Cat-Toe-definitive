cellImage(cell) {
    if (cell === this.PLAYER_1) {
        return "img/player1.png";
    } else if (cell === this.PLAYER_2) {
        return "img/player2.png";
    } else {
        return "img/empty.png"
    }
},

const COLUMNS = 7,
ROWS = 6,
EMPTY_SPACE = " ",
PLAYER_1 = "o",
PLAYER_2 = "x",
PLAYER_CPU = PLAYER_2,
CONNECT = 4; // <-- Change this and you can play connect 5, connect 3, connect 100 and so on!
