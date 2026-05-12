





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int value;
    private String suit;





    private Deck deck;


    public Card(
        int value,        String suit    ) {
        this.value = value;
        this.suit = suit;
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

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}