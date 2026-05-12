





import java.util.List;
import java.util.ArrayList;

public class Membership_Card  {

    private int ID;
    private int DiscountLVL;





    private List<Order> orders;


    public Membership_Card(
        int ID,        int DiscountLVL    ) {
        this.ID = ID;
        this.DiscountLVL = DiscountLVL;
        this.orders = new ArrayList<>();
    }

    public Membership_Card(
        int ID,        int DiscountLVL        ArrayList<Order> orders    ) {
        this.ID = ID;
        this.DiscountLVL = DiscountLVL;
        this.orders = orders;
    }

    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public int getDiscountlvl() {
        return DiscountLVL;
    }

    public void setDiscountlvl(int DiscountLVL) {
        this.DiscountLVL = DiscountLVL;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}