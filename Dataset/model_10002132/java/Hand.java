





import java.util.List;
import java.util.ArrayList;

public class Hand  {

    private int startHand;





    private List<Card> cards;




    private BlackJack blackjack;




    private BlackJack blackjack;




    private Dealer dealer;


    public Hand(
        int startHand    ) {
        this.startHand = startHand;
        this.cards = new ArrayList<>();
    }

    public Hand(
        int startHand        ArrayList<Card> cards    ) {
        this.startHand = startHand;
        this.cards = cards;
    }

    public int getStarthand() {
        return startHand;
    }

    public void setStarthand(int startHand) {
        this.startHand = startHand;
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
    public BlackJack getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(BlackJack blackjack) {
        this.blackjack = blackjack;
    }
    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }

}