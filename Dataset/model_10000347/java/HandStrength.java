





import java.util.List;
import java.util.ArrayList;

public class HandStrength  {

    private int STRAIGHT_FLUSH;





    private Dealer dealer;


    public HandStrength(
        int STRAIGHT_FLUSH    ) {
        this.STRAIGHT_FLUSH = STRAIGHT_FLUSH;
    }


    public int getStraight_flush() {
        return STRAIGHT_FLUSH;
    }

    public void setStraight_flush(int STRAIGHT_FLUSH) {
        this.STRAIGHT_FLUSH = STRAIGHT_FLUSH;
    }

    public Dealer getDealer() {
        return dealer;
    }

    public void setDealer(Dealer dealer) {
        this.dealer = dealer;
    }

}