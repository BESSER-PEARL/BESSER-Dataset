





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int face;
    private String suit;



    public Card(
        int face,        String suit    ) {
        this.face = face;
        this.suit = suit;
    }


    public int getFace() {
        return face;
    }

    public void setFace(int face) {
        this.face = face;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }


}