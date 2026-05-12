





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String deck;
    private String deckNumber;



    public Deck(
        String deck,        String deckNumber    ) {
        this.deck = deck;
        this.deckNumber = deckNumber;
    }


    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public String getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(String deckNumber) {
        this.deckNumber = deckNumber;
    }


}