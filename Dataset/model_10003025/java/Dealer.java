





import java.util.List;
import java.util.ArrayList;

public class Dealer  {

    private int cardTotalLimit;
    private None hand;



    public Dealer(
        int cardTotalLimit,        None hand    ) {
        this.cardTotalLimit = cardTotalLimit;
        this.hand = hand;
    }


    public int getCardtotallimit() {
        return cardTotalLimit;
    }

    public void setCardtotallimit(int cardTotalLimit) {
        this.cardTotalLimit = cardTotalLimit;
    }
    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }


}