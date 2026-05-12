





import java.util.List;
import java.util.ArrayList;

public class Checkout  {

    private int checkoutID;
    private float checkoutAmount;





    private Order order;


    public Checkout(
        int checkoutID,        float checkoutAmount    ) {
        this.checkoutID = checkoutID;
        this.checkoutAmount = checkoutAmount;
    }


    public int getCheckoutid() {
        return checkoutID;
    }

    public void setCheckoutid(int checkoutID) {
        this.checkoutID = checkoutID;
    }
    public float getCheckoutamount() {
        return checkoutAmount;
    }

    public void setCheckoutamount(float checkoutAmount) {
        this.checkoutAmount = checkoutAmount;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}