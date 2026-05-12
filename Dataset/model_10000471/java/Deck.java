





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String cards;





    private List<Card> cards;


    public Deck(
        String cards    ) {
        this.cards = cards;
        this.cards = new ArrayList<>();
    }

    public Deck(
        String cards        ArrayList<Card> cards    ) {
        this.cards = cards;
        this.cards = cards;
    }

    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}