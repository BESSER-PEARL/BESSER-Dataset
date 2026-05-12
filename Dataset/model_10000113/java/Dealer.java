





import java.util.List;
import java.util.ArrayList;

public class Dealer  {

    private None hand;
    private int cardTotalLimit;





    private Hand hand;


    public Dealer(
        None hand,        int cardTotalLimit    ) {
        this.hand = hand;
        this.cardTotalLimit = cardTotalLimit;
    }


    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public int getCardtotallimit() {
        return cardTotalLimit;
    }

    public void setCardtotallimit(int cardTotalLimit) {
        this.cardTotalLimit = cardTotalLimit;
    }

    public Hand getHand() {
        return hand;
    }

    public void setHand(Hand hand) {
        this.hand = hand;
    }

}