





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String deck;
    private String cardsDealt;





    private Card card;


    public Deck(
        String deck,        String cardsDealt    ) {
        this.deck = deck;
        this.cardsDealt = cardsDealt;
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

}