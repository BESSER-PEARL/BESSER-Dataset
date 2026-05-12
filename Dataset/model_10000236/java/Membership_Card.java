





import java.util.List;
import java.util.ArrayList;

public class Membership_Card  {

    private int DiscountLVL;
    private int ID;





    private List<Order> orders;


    public Membership_Card(
        int DiscountLVL,        int ID    ) {
        this.DiscountLVL = DiscountLVL;
        this.ID = ID;
        this.orders = new ArrayList<>();
    }

    public Membership_Card(
        int DiscountLVL,        int ID        ArrayList<Order> orders    ) {
        this.DiscountLVL = DiscountLVL;
        this.ID = ID;
        this.orders = orders;
    }

    public int getDiscountlvl() {
        return DiscountLVL;
    }

    public void setDiscountlvl(int DiscountLVL) {
        this.DiscountLVL = DiscountLVL;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}