





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int value;
    private String display;
    private int suit;
    private boolean faceUp;



    public Card(
        int value,        String display,        int suit,        boolean faceUp    ) {
        this.value = value;
        this.display = display;
        this.suit = suit;
        this.faceUp = faceUp;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getDisplay() {
        return display;
    }

    public void setDisplay(String display) {
        this.display = display;
    }
    public int getSuit() {
        return suit;
    }

    public void setSuit(int suit) {
        this.suit = suit;
    }
    public boolean getFaceup() {
        return faceUp;
    }

    public void setFaceup(boolean faceUp) {
        this.faceUp = faceUp;
    }


}