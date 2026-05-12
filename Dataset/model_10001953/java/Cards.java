





import java.util.List;
import java.util.ArrayList;

public class Cards  {

    private None title;
    private int value;
    private None suit;





    private Deck deck;


    public Cards(
        None title,        int value,        None suit    ) {
        this.title = title;
        this.value = value;
        this.suit = suit;
    }


    public None getTitle() {
        return title;
    }

    public void setTitle(None title) {
        this.title = title;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}