





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private String type;
    private int id;





    private List<Order> orders;


    public Product(
        String name,        String type,        int id    ) {
        this.name = name;
        this.type = type;
        this.id = id;
        this.orders = new ArrayList<>();
    }

    public Product(
        String name,        String type,        int id        ArrayList<Order> orders    ) {
        this.name = name;
        this.type = type;
        this.id = id;
        this.orders = orders;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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