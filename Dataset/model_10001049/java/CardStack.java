





import java.util.List;
import java.util.ArrayList;

public class CardStack  {






    private List<Card> cards;


    public CardStack(
    ) {
        this.cards = new ArrayList<>();
    }

    public CardStack(
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