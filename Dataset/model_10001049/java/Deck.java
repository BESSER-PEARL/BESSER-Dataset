





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private int deckNumber;





    private List<Card> cards;


    public Deck(
        int deckNumber    ) {
        this.deckNumber = deckNumber;
        this.cards = new ArrayList<>();
    }

    public Deck(
        int deckNumber        ArrayList<Card> cards    ) {
        this.deckNumber = deckNumber;
        this.cards = cards;
    }

    public int getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(int deckNumber) {
        this.deckNumber = deckNumber;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}