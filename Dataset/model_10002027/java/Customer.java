





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private int customerID;
    private int phoneNumber;





    private List<Order> orders;




    private Store store;


    public Customer(
        String name,        int customerID,        int phoneNumber    ) {
        this.name = name;
        this.customerID = customerID;
        this.phoneNumber = phoneNumber;
        this.orders = new ArrayList<>();
    }

    public Customer(
        String name,        int customerID,        int phoneNumber        ArrayList<Order> orders    ) {
        this.name = name;
        this.customerID = customerID;
        this.phoneNumber = phoneNumber;
        this.orders = orders;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCustomerid() {
        return customerID;
    }

    public void setCustomerid(int customerID) {
        this.customerID = customerID;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
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