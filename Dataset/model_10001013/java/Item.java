





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private int item_code;
    private String item_name;





    private List<Order> orders;


    public Item(
        int item_code,        String item_name    ) {
        this.item_code = item_code;
        this.item_name = item_name;
        this.orders = new ArrayList<>();
    }

    public Item(
        int item_code,        String item_name        ArrayList<Order> orders    ) {
        this.item_code = item_code;
        this.item_name = item_name;
        this.orders = orders;
    }

    public int getItem_code() {
        return item_code;
    }

    public void setItem_code(int item_code) {
        this.item_code = item_code;
    }
    public String getItem_name() {
        return item_name;
    }

    public void setItem_name(String item_name) {
        this.item_name = item_name;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}