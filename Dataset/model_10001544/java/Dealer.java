





import java.util.List;
import java.util.ArrayList;

public class Dealer  {

    private int handValue;
    private int handLimit;



    public Dealer(
        int handValue,        int handLimit    ) {
        this.handValue = handValue;
        this.handLimit = handLimit;
    }


    public int getHandvalue() {
        return handValue;
    }

    public void setHandvalue(int handValue) {
        this.handValue = handValue;
    }
    public int getHandlimit() {
        return handLimit;
    }

    public void setHandlimit(int handLimit) {
        this.handLimit = handLimit;
    }


}