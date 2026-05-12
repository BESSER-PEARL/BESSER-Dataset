





import java.util.List;
import java.util.ArrayList;

public class Connect4_Player  {

    private boolean currentPlayer;
    private String name;
    private int wins;
    private boolean roundWon;
    private String tokenColor;





    private Connect4_Board connect4_board;


    public Connect4_Player(
        boolean currentPlayer,        String name,        int wins,        boolean roundWon,        String tokenColor    ) {
        this.currentPlayer = currentPlayer;
        this.name = name;
        this.wins = wins;
        this.roundWon = roundWon;
        this.tokenColor = tokenColor;
    }


    public boolean getCurrentplayer() {
        return currentPlayer;
    }

    public void setCurrentplayer(boolean currentPlayer) {
        this.currentPlayer = currentPlayer;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getWins() {
        return wins;
    }

    public void setWins(int wins) {
        this.wins = wins;
    }
    public boolean getRoundwon() {
        return roundWon;
    }

    public void setRoundwon(boolean roundWon) {
        this.roundWon = roundWon;
    }
    public String getTokencolor() {
        return tokenColor;
    }

    public void setTokencolor(String tokenColor) {
        this.tokenColor = tokenColor;
    }

    public Connect4_Board getConnect4_board() {
        return connect4_board;
    }

    public void setConnect4_board(Connect4_Board connect4_board) {
        this.connect4_board = connect4_board;
    }

}