





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String cards;
    private int value;
    private String suit;



    public Card(
        String cards,        int value,        String suit    ) {
        this.cards = cards;
        this.value = value;
        this.suit = suit;
    }


    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }


}