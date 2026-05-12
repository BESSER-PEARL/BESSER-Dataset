





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String deck;





    private List<Card> cards;


    public Deck(
        String deck    ) {
        this.deck = deck;
        this.cards = new ArrayList<>();
    }

    public Deck(
        String deck        ArrayList<Card> cards    ) {
        this.deck = deck;
        this.cards = cards;
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