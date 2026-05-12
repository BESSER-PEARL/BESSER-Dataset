





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String type;
    private int id;
    private String name;





    private List<Order> orders;


    public Product(
        String type,        int id,        String name    ) {
        this.type = type;
        this.id = id;
        this.name = name;
        this.orders = new ArrayList<>();
    }

    public Product(
        String type,        int id,        String name        ArrayList<Order> orders    ) {
        this.type = type;
        this.id = id;
        this.name = name;
        this.orders = orders;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}