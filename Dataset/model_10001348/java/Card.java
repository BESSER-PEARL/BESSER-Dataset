





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int suit;
    private int rank;
    private int points;
    private boolean isDouble;



    public Card(
        int suit,        int rank,        int points,        boolean isDouble    ) {
        this.suit = suit;
        this.rank = rank;
        this.points = points;
        this.isDouble = isDouble;
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
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }
    public boolean getIsdouble() {
        return isDouble;
    }

    public void setIsdouble(boolean isDouble) {
        this.isDouble = isDouble;
    }


}