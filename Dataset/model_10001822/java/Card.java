





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private boolean isDouble;
    private int rank;
    private int points;
    private int suit;



    public Card(
        boolean isDouble,        int rank,        int points,        int suit    ) {
        this.isDouble = isDouble;
        this.rank = rank;
        this.points = points;
        this.suit = suit;
    }


    public boolean getIsdouble() {
        return isDouble;
    }

    public void setIsdouble(boolean isDouble) {
        this.isDouble = isDouble;
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
    public int getSuit() {
        return suit;
    }

    public void setSuit(int suit) {
        this.suit = suit;
    }


}