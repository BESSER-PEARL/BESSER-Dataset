





import java.util.List;
import java.util.ArrayList;

public class card_Card  {

    private int suit;
    private int rank;



    public card_Card(
        int suit,        int rank    ) {
        this.suit = suit;
        this.rank = rank;
    }


    public int getSuit() {
        return suit;
    }

    public void setSuit(int suit) {
        this.suit = suit;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }


}