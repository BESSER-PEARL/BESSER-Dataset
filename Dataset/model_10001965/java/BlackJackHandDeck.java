





import java.util.List;
import java.util.ArrayList;

public class BlackJackHandDeck  {

    private int MAX_SCORE;
    private boolean stand;
    private int wager;



    public BlackJackHandDeck(
        int MAX_SCORE,        boolean stand,        int wager    ) {
        this.MAX_SCORE = MAX_SCORE;
        this.stand = stand;
        this.wager = wager;
    }


    public int getMax_score() {
        return MAX_SCORE;
    }

    public void setMax_score(int MAX_SCORE) {
        this.MAX_SCORE = MAX_SCORE;
    }
    public boolean getStand() {
        return stand;
    }

    public void setStand(boolean stand) {
        this.stand = stand;
    }
    public int getWager() {
        return wager;
    }

    public void setWager(int wager) {
        this.wager = wager;
    }


}