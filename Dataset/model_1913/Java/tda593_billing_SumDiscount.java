





import java.util.List;
import java.util.ArrayList;

public class tda593_billing_SumDiscount extends Discount {

    private float discountSum;



    public tda593_billing_SumDiscount(
        float discountSum    ) {
        super(
        );
        this.discountSum = discountSum;
    }


    public float getDiscountsum() {
        return discountSum;
    }

    public void setDiscountsum(float discountSum) {
        this.discountSum = discountSum;
    }


}