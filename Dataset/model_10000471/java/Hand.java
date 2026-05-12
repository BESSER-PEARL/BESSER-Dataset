





import java.util.List;
import java.util.ArrayList;

public class Hand  {

    private String handCollection;





    private List<Card> cards;


    public Hand(
        String handCollection    ) {
        this.handCollection = handCollection;
        this.cards = new ArrayList<>();
    }

    public Hand(
        String handCollection        ArrayList<Card> cards    ) {
        this.handCollection = handCollection;
        this.cards = cards;
    }

    public String getHandcollection() {
        return handCollection;
    }

    public void setHandcollection(String handCollection) {
        this.handCollection = handCollection;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}