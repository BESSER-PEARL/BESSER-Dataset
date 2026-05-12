





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int Order_id;
    private int Cust_id;





    private Customer customer;


    public Order(
        int Order_id,        int Cust_id    ) {
        this.Order_id = Order_id;
        this.Cust_id = Cust_id;
    }


    public int getOrder_id() {
        return Order_id;
    }

    public void setOrder_id(int Order_id) {
        this.Order_id = Order_id;
    }
    public int getCust_id() {
        return Cust_id;
    }

    public void setCust_id(int Cust_id) {
        this.Cust_id = Cust_id;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}