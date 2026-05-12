





import java.util.List;
import java.util.ArrayList;

public class Poker_PokerGame  {

    private int Round;
    private int numPlayers;



    public Poker_PokerGame(
        int Round,        int numPlayers    ) {
        this.Round = Round;
        this.numPlayers = numPlayers;
    }


    public int getRound() {
        return Round;
    }

    public void setRound(int Round) {
        this.Round = Round;
    }
    public int getNumplayers() {
        return numPlayers;
    }

    public void setNumplayers(int numPlayers) {
        this.numPlayers = numPlayers;
    }


}