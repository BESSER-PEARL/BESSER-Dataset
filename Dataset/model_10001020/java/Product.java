





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private int id;
    private String type;





    private List<Order> orders;


    public Product(
        String name,        int id,        String type    ) {
        this.name = name;
        this.id = id;
        this.type = type;
        this.orders = new ArrayList<>();
    }

    public Product(
        String name,        int id,        String type        ArrayList<Order> orders    ) {
        this.name = name;
        this.id = id;
        this.type = type;
        this.orders = orders;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}