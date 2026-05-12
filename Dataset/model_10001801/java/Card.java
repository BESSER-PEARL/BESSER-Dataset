





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String front;
    private String suit;
    private String value;



    public Card(
        String front,        String suit,        String value    ) {
        this.front = front;
        this.suit = suit;
        this.value = value;
    }


    public String getFront() {
        return front;
    }

    public void setFront(String front) {
        this.front = front;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}