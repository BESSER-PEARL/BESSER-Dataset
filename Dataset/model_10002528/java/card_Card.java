





import java.util.List;
import java.util.ArrayList;

public class card_Card  {

    private int rank;
    private int suit;



    public card_Card(
        int rank,        int suit    ) {
        this.rank = rank;
        this.suit = suit;
    }


    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public int getSuit() {
        return suit;
    }

    public void setSuit(int suit) {
        this.suit = suit;
    }


}