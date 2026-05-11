





import java.util.List;
import java.util.ArrayList;

public class ordersystem_Customer  {

    private String firstName;
    private String lastName;





    private List<ordersystem_Order> ordersystem_orders;




    private ordersystem_Order ordersystem_order;


    public ordersystem_Customer(
        String firstName,        String lastName    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.ordersystem_orders = new ArrayList<>();
    }

    public ordersystem_Customer(
        String firstName,        String lastName        ArrayList<ordersystem_Order> ordersystem_orders    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.ordersystem_orders = ordersystem_orders;
    }

    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public List<ordersystem_Order> getOrdersystem_orders() {
        return ordersystem_orders;
    }

    public void addOrdersystem_order(Ordersystem_order ordersystem_order) {
        this.ordersystem_orders.add(ordersystem_order);
    }
    public ordersystem_Order getOrdersystem_order() {
        return ordersystem_order;
    }

    public void setOrdersystem_order(ordersystem_Order ordersystem_order) {
        this.ordersystem_order = ordersystem_order;
    }

}