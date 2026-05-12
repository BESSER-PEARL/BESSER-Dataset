





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String suit;
    private int face;



    public Card(
        String suit,        int face    ) {
        this.suit = suit;
        this.face = face;
    }


    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public int getFace() {
        return face;
    }

    public void setFace(int face) {
        this.face = face;
    }


}