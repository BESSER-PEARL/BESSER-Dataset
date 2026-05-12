





import java.util.List;
import java.util.ArrayList;

public class Dealer  {

    private String name;
    private None cards;





    private Deck deck;


    public Dealer(
        String name,        None cards    ) {
        this.name = name;
        this.cards = cards;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getCards() {
        return cards;
    }

    public void setCards(None cards) {
        this.cards = cards;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}