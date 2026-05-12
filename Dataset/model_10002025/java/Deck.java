





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String CardsList;





    private List<Card> cards;


    public Deck(
        String CardsList    ) {
        this.CardsList = CardsList;
        this.cards = new ArrayList<>();
    }

    public Deck(
        String CardsList        ArrayList<Card> cards    ) {
        this.CardsList = CardsList;
        this.cards = cards;
    }

    public String getCardslist() {
        return CardsList;
    }

    public void setCardslist(String CardsList) {
        this.CardsList = CardsList;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }

}