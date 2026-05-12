





import java.util.List;
import java.util.ArrayList;

public class Card2  {

    private None suit;
    private None kind;





    private Deck2 deck2;


    public Card2(
        None suit,        None kind    ) {
        this.suit = suit;
        this.kind = kind;
    }


    public None getSuit() {
        return suit;
    }

    public void setSuit(None suit) {
        this.suit = suit;
    }
    public None getKind() {
        return kind;
    }

    public void setKind(None kind) {
        this.kind = kind;
    }

    public Deck2 getDeck2() {
        return deck2;
    }

    public void setDeck2(Deck2 deck2) {
        this.deck2 = deck2;
    }

}