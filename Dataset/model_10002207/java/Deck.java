





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private None deck;
    private int cardsUsed;





    private List<Card> cards;




    private BlackJack blackjack;


    public Deck(
        None deck,        int cardsUsed    ) {
        this.deck = deck;
        this.cardsUsed = cardsUsed;
        this.cards = new ArrayList<>();
    }

    public Deck(
        None deck,        int cardsUsed        ArrayList<Card> cards    ) {
        this.deck = deck;
        this.cardsUsed = cardsUsed;
        this.cards = cards;
    }

    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public int getCardsused() {
        return cardsUsed;
    }

    public void setCardsused(int cardsUsed) {
        this.cardsUsed = cardsUsed;
    }

    public List<Card> getCards() {
        return cards;
    }

    public void addCard(Card card) {
        this.cards.add(card);
    }
    public BlackJack getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(BlackJack blackjack) {
        this.blackjack = blackjack;
    }

}