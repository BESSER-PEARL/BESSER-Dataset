





import java.util.List;
import java.util.ArrayList;

public class ExtensionBoard  {






    private List<Card> cards;


    public ExtensionBoard(
    ) {
        this.cards = new ArrayList<>();
    }

    public ExtensionBoard(
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