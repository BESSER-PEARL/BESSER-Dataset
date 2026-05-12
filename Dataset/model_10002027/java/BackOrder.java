





import java.util.List;
import java.util.ArrayList;

public class BackOrder  {

    private None backOrderList;





    private List<Order> orders;




    private Store store;


    public BackOrder(
        None backOrderList    ) {
        this.backOrderList = backOrderList;
        this.orders = new ArrayList<>();
    }

    public BackOrder(
        None backOrderList        ArrayList<Order> orders    ) {
        this.backOrderList = backOrderList;
        this.orders = orders;
    }

    public None getBackorderlist() {
        return backOrderList;
    }

    public void setBackorderlist(None backOrderList) {
        this.backOrderList = backOrderList;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }
    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }

}