





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String deck;
    private String usedCards;





    private List<Card> cards;


    public Deck(
        String deck,        String usedCards    ) {
        this.deck = deck;
        this.usedCards = usedCards;
        this.cards = new ArrayList<>();
    }

    public Deck(
        String deck,        String usedCards        ArrayList<Card> cards    ) {
        this.deck = deck;
        this.usedCards = usedCards;
        this.cards = cards;
    }

    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public String getUsedcards() {
        return usedCards;
    }

    public void setUsedcards(String usedCards) {
        this.usedCards = usedCards;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}