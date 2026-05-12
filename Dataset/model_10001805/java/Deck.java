





import java.util.List;
import java.util.ArrayList;

public class Deck  {






    private List<Card> cards;


    public Deck(
    ) {
        this.cards = new ArrayList<>();
    }

    public Deck(
        ArrayList<Card> cards    ) {
        this.cards = cards;
    }


    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}