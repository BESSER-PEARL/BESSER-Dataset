





import java.util.List;
import java.util.ArrayList;

public class PurchaseAmountSlab  {

    private float from;
    private float discount;
    private float to;



    public PurchaseAmountSlab(
        float from,        float discount,        float to    ) {
        this.from = from;
        this.discount = discount;
        this.to = to;
    }


    public float getFrom() {
        return from;
    }

    public void setFrom(float from) {
        this.from = from;
    }
    public float getDiscount() {
        return discount;
    }

    public void setDiscount(float discount) {
        this.discount = discount;
    }
    public float getTo() {
        return to;
    }

    public void setTo(float to) {
        this.to = to;
    }


}