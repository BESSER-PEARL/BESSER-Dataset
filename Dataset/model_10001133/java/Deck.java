





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String deck;
    private int size;





    private List<Card> cards;


    public Deck(
        String deck,        int size    ) {
        this.deck = deck;
        this.size = size;
        this.cards = new ArrayList<>();
    }

    public Deck(
        String deck,        int size        ArrayList<Card> cards    ) {
        this.deck = deck;
        this.size = size;
        this.cards = cards;
    }

    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}