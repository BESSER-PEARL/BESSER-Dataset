





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String type;
    private String name;
    private int id;





    private List<Order> orders;


    public Product(
        String type,        String name,        int id    ) {
        this.type = type;
        this.name = name;
        this.id = id;
        this.orders = new ArrayList<>();
    }

    public Product(
        String type,        String name,        int id        ArrayList<Order> orders    ) {
        this.type = type;
        this.name = name;
        this.id = id;
        this.orders = orders;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}