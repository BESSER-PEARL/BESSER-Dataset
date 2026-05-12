





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int id;
    private String name;
    private String type;





    private List<Admin> admins;




    private List<Order> orders;


    public Product(
        int id,        String name,        String type    ) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.admins = new ArrayList<>();
        this.orders = new ArrayList<>();
    }

    public Product(
        int id,        String name,        String type        ArrayList<Admin> admins,        ArrayList<Order> orders    ) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.admins = admins;
        this.orders = orders;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }
    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}