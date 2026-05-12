





import java.util.List;
import java.util.ArrayList;

public class Store  {

    private String orders;
    private String inventory;
    private String customers;
    private String sales;





    private List<Order> orders;


    public Store(
        String orders,        String inventory,        String customers,        String sales    ) {
        this.orders = orders;
        this.inventory = inventory;
        this.customers = customers;
        this.sales = sales;
        this.orders = new ArrayList<>();
    }

    public Store(
        String orders,        String inventory,        String customers,        String sales        ArrayList<Order> orders    ) {
        this.orders = orders;
        this.inventory = inventory;
        this.customers = customers;
        this.sales = sales;
        this.orders = orders;
    }

    public String getOrders() {
        return orders;
    }

    public void setOrders(String orders) {
        this.orders = orders;
    }
    public String getInventory() {
        return inventory;
    }

    public void setInventory(String inventory) {
        this.inventory = inventory;
    }
    public String getCustomers() {
        return customers;
    }

    public void setCustomers(String customers) {
        this.customers = customers;
    }
    public String getSales() {
        return sales;
    }

    public void setSales(String sales) {
        this.sales = sales;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}