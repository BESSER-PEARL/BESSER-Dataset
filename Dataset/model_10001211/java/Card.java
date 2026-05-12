





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String suit;
    private int value;



    public Card(
        String suit,        int value    ) {
        this.suit = suit;
        this.value = value;
    }


    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}