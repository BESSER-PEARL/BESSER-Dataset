





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private int size;
    private String deck;





    private List<Card> cards;


    public Deck(
        int size,        String deck    ) {
        this.size = size;
        this.deck = deck;
        this.cards = new ArrayList<>();
    }

    public Deck(
        int size,        String deck        ArrayList<Card> cards    ) {
        this.size = size;
        this.deck = deck;
        this.cards = cards;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}