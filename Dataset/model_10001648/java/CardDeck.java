





import java.util.List;
import java.util.ArrayList;

public class CardDeck  {

    private String suits;
    private String cards;





    private List<Card> cards;


    public CardDeck(
        String suits,        String cards    ) {
        this.suits = suits;
        this.cards = cards;
        this.cards = new ArrayList<>();
    }

    public CardDeck(
        String suits,        String cards        ArrayList<Card> cards    ) {
        this.suits = suits;
        this.cards = cards;
        this.cards = cards;
    }

    public String getSuits() {
        return suits;
    }

    public void setSuits(String suits) {
        this.suits = suits;
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