





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int CustNumber;





    private List<Order> orders;


    public Customer(
        int CustNumber    ) {
        this.CustNumber = CustNumber;
        this.orders = new ArrayList<>();
    }

    public Customer(
        int CustNumber        ArrayList<Order> orders    ) {
        this.CustNumber = CustNumber;
        this.orders = orders;
    }

    public int getCustnumber() {
        return CustNumber;
    }

    public void setCustnumber(int CustNumber) {
        this.CustNumber = CustNumber;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}