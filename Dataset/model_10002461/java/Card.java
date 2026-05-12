





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private None kind;
    private None suit;





    private Deck deck;


    public Card(
        None kind,        None suit    ) {
        this.kind = kind;
        this.suit = suit;
    }


    public None getKind() {
        return kind;
    }

    public void setKind(None kind) {
        this.kind = kind;
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