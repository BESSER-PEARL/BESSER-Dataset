





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private None Suit;
    private int Rank;



    public Card(
        None Suit,        int Rank    ) {
        this.Suit = Suit;
        this.Rank = Rank;
    }


    public None getSuit() {
        return Suit;
    }

    public void setSuit(None Suit) {
        this.Suit = Suit;
    }
    public int getRank() {
        return Rank;
    }

    public void setRank(int Rank) {
        this.Rank = Rank;
    }


}