





import java.util.List;
import java.util.ArrayList;

public class SpecialOrder  {

    private int offerCode;
    private int orderRange;



    public SpecialOrder(
        int offerCode,        int orderRange    ) {
        this.offerCode = offerCode;
        this.orderRange = orderRange;
    }


    public int getOffercode() {
        return offerCode;
    }

    public void setOffercode(int offerCode) {
        this.offerCode = offerCode;
    }
    public int getOrderrange() {
        return orderRange;
    }

    public void setOrderrange(int orderRange) {
        this.orderRange = orderRange;
    }


}