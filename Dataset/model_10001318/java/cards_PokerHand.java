





import java.util.List;
import java.util.ArrayList;

public class cards_PokerHand  {

    private String hand;
    private int rank;



    public cards_PokerHand(
        String hand,        int rank    ) {
        this.hand = hand;
        this.rank = rank;
    }


    public String getHand() {
        return hand;
    }

    public void setHand(String hand) {
        this.hand = hand;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }


}