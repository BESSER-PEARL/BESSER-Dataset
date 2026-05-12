





import java.util.List;
import java.util.ArrayList;

public class Membership  {

    private float discount;
    private int loyaltyID;





    private Checkout checkout;


    public Membership(
        float discount,        int loyaltyID    ) {
        this.discount = discount;
        this.loyaltyID = loyaltyID;
    }


    public float getDiscount() {
        return discount;
    }

    public void setDiscount(float discount) {
        this.discount = discount;
    }
    public int getLoyaltyid() {
        return loyaltyID;
    }

    public void setLoyaltyid(int loyaltyID) {
        this.loyaltyID = loyaltyID;
    }

    public Checkout getCheckout() {
        return checkout;
    }

    public void setCheckout(Checkout checkout) {
        this.checkout = checkout;
    }

}