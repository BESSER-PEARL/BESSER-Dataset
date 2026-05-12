





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String deck;
    private String cardsDealt;





    private Card card;




    private List_Card__external list_card__external;


    public Deck(
        String deck,        String cardsDealt    ) {
        this.deck = deck;
        this.cardsDealt = cardsDealt;
        this.list_card__externals = new ArrayList<>();
    }


    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public String getCardsdealt() {
        return cardsDealt;
    }

    public void setCardsdealt(String cardsDealt) {
        this.cardsDealt = cardsDealt;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }
    public List_Card__external getList_card__externals() {
        return list_card__externals;
    }

    public void addList_card__external(List_card__external list_card__external) {
        this.list_card__externals.add(list_card__external);
    }

}