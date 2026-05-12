





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int suit;
    private int value;
    private boolean color;





    private Deck deck;


    public Card(
        int suit,        int value,        boolean color    ) {
        this.suit = suit;
        this.value = value;
        this.color = color;
    }


    public int getSuit() {
        return suit;
    }

    public void setSuit(int suit) {
        this.suit = suit;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public boolean getColor() {
        return color;
    }

    public void setColor(boolean color) {
        this.color = color;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}