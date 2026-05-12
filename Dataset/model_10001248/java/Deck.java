





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String cards;
    private int positionInDeck;



    public Deck(
        String cards,        int positionInDeck    ) {
        this.cards = cards;
        this.positionInDeck = positionInDeck;
    }


    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }
    public int getPositionindeck() {
        return positionInDeck;
    }

    public void setPositionindeck(int positionInDeck) {
        this.positionInDeck = positionInDeck;
    }


}