





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int suit;
    private int face;



    public Card(
        int suit,        int face    ) {
        this.suit = suit;
        this.face = face;
    }


    public int getSuit() {
        return suit;
    }

    public void setSuit(int suit) {
        this.suit = suit;
    }
    public int getFace() {
        return face;
    }

    public void setFace(int face) {
        this.face = face;
    }


}