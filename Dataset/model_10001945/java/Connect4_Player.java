





import java.util.List;
import java.util.ArrayList;

public class Connect4_Player  {

    private String name;
    private boolean roundWon;
    private boolean currentPlayer;
    private String tokenColor;
    private int wins;



    public Connect4_Player(
        String name,        boolean roundWon,        boolean currentPlayer,        String tokenColor,        int wins    ) {
        this.name = name;
        this.roundWon = roundWon;
        this.currentPlayer = currentPlayer;
        this.tokenColor = tokenColor;
        this.wins = wins;
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
    public boolean getCurrentplayer() {
        return currentPlayer;
    }

    public void setCurrentplayer(boolean currentPlayer) {
        this.currentPlayer = currentPlayer;
    }
    public String getTokencolor() {
        return tokenColor;
    }

    public void setTokencolor(String tokenColor) {
        this.tokenColor = tokenColor;
    }
    public int getWins() {
        return wins;
    }

    public void setWins(int wins) {
        this.wins = wins;
    }


}