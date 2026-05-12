





import java.util.List;
import java.util.ArrayList;

public class cards_Card  {

    private int rank;
    private None suit;



    public cards_Card(
        int rank,        None suit    ) {
        this.rank = rank;
        this.suit = suit;
    }


    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }


}