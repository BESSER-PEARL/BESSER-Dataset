





import java.util.List;
import java.util.ArrayList;

public class Sprint  {






    private List<Card> cards;


    public Sprint(
    ) {
        this.cards = new ArrayList<>();
    }

    public Sprint(
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