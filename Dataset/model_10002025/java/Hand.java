





import java.util.List;
import java.util.ArrayList;

public class Hand  {

    private String HandOfCards;





    private List<Card> cards;


    public Hand(
        String HandOfCards    ) {
        this.HandOfCards = HandOfCards;
        this.cards = new ArrayList<>();
    }

    public Hand(
        String HandOfCards        ArrayList<Card> cards    ) {
        this.HandOfCards = HandOfCards;
        this.cards = cards;
    }

    public String getHandofcards() {
        return HandOfCards;
    }

    public void setHandofcards(String HandOfCards) {
        this.HandOfCards = HandOfCards;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}