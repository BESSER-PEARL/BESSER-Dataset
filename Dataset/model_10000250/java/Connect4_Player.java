





import java.util.List;
import java.util.ArrayList;

public class Connect4_Player  {

    private int wins;
    private String tokenColor;
    private boolean currentPlayer;
    private String name;
    private boolean roundWon;



    public Connect4_Player(
        int wins,        String tokenColor,        boolean currentPlayer,        String name,        boolean roundWon    ) {
        this.wins = wins;
        this.tokenColor = tokenColor;
        this.currentPlayer = currentPlayer;
        this.name = name;
        this.roundWon = roundWon;
    }


    public int getWins() {
        return wins;
    }

    public void setWins(int wins) {
        this.wins = wins;
    }
    public String getTokencolor() {
        return tokenColor;
    }

    public void setTokencolor(String tokenColor) {
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
    public boolean getRoundwon() {
        return roundWon;
    }

    public void setRoundwon(boolean roundWon) {
        this.roundWon = roundWon;
    }


}