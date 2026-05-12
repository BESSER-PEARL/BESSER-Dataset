





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private None suit;
    private None rank;



    public Card(
        None suit,        None rank    ) {
        this.suit = suit;
        this.rank = rank;
    }


    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }
    public None getRank() {
        return rank;
    }

    public void setRank(None rank) {
        this.rank = rank;
    }


}