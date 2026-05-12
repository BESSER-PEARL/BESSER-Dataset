





import java.util.List;
import java.util.ArrayList;

public class Membership_Card  {

    private int Discount;
    private int LoyaltyID;





    private List<OrderController> ordercontrollers;


    public Membership_Card(
        int Discount,        int LoyaltyID    ) {
        this.Discount = Discount;
        this.LoyaltyID = LoyaltyID;
        this.ordercontrollers = new ArrayList<>();
    }

    public Membership_Card(
        int Discount,        int LoyaltyID        ArrayList<OrderController> ordercontrollers    ) {
        this.Discount = Discount;
        this.LoyaltyID = LoyaltyID;
        this.ordercontrollers = ordercontrollers;
    }

    public int getDiscount() {
        return Discount;
    }

    public void setDiscount(int Discount) {
        this.Discount = Discount;
    }
    public int getLoyaltyid() {
        return LoyaltyID;
    }

    public void setLoyaltyid(int LoyaltyID) {
        this.LoyaltyID = LoyaltyID;
    }

    public List<OrderController> getOrdercontrollers() {
        return ordercontrollers;
    }

    public void addOrdercontroller(Ordercontroller ordercontroller) {
        this.ordercontrollers.add(ordercontroller);
    }

}