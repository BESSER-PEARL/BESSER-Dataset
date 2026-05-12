





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String rank;
    private int pointValue;
    private String suit;



    public Card(
        String rank,        int pointValue,        String suit    ) {
        this.rank = rank;
        this.pointValue = pointValue;
        this.suit = suit;
    }


    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }
    public int getPointvalue() {
        return pointValue;
    }

    public void setPointvalue(int pointValue) {
        this.pointValue = pointValue;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }


}