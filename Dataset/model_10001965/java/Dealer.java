





import java.util.List;
import java.util.ArrayList;

public class Dealer  {

    private None hand;





    private BlackJackHandDeck blackjackhanddeck;


    public Dealer(
        None hand    ) {
        this.hand = hand;
    }


    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }

    public BlackJackHandDeck getBlackjackhanddeck() {
        return blackjackhanddeck;
    }

    public void setBlackjackhanddeck(BlackJackHandDeck blackjackhanddeck) {
        this.blackjackhanddeck = blackjackhanddeck;
    }

}