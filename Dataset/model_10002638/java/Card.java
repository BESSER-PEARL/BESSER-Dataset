





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private None rank;
    private None suit;



    public Card(
        None rank,        None suit    ) {
        this.rank = rank;
        this.suit = suit;
    }


    public None getRank() {
        return rank;
    }

    public void setRank(None rank) {
        this.rank = rank;
    }
    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }


}