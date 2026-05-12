





import java.util.List;
import java.util.ArrayList;

public class Deck  {






    private Deck deck;




    private Dealer dealer;




    private List<Card> cards;




    private BlackJack blackjack;


    public Deck(
    ) {
        this.cards = new ArrayList<>();
    }

    public Deck(
        ArrayList<Card> cards    ) {
        this.cards = cards;
    }


    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
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