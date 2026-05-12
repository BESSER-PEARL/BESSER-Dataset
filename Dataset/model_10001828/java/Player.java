





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int losses;
    private int wins;
    private String winRate;





    private Elevens elevens;


    public Player(
        int losses,        int wins,        String winRate    ) {
        this.losses = losses;
        this.wins = wins;
        this.winRate = winRate;
    }


    public int getLosses() {
        return losses;
    }

    public void setLosses(int losses) {
        this.losses = losses;
    }
    public int getWins() {
        return wins;
    }

    public void setWins(int wins) {
        this.wins = wins;
    }
    public String getWinrate() {
        return winRate;
    }

    public void setWinrate(String winRate) {
        this.winRate = winRate;
    }

    public Elevens getElevens() {
        return elevens;
    }

    public void setElevens(Elevens elevens) {
        this.elevens = elevens;
    }

}