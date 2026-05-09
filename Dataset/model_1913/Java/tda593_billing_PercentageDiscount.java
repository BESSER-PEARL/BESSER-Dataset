





import java.util.List;
import java.util.ArrayList;

public class tda593_billing_PercentageDiscount extends Discount {

    private float percentage;



    public tda593_billing_PercentageDiscount(
        float percentage    ) {
        super(
        );
        this.percentage = percentage;
    }


    public float getPercentage() {
        return percentage;
    }

    public void setPercentage(float percentage) {
        this.percentage = percentage;
    }


}