





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int Order_ID;





    private Payment payment;




    private Customer customer;


    public Order(
        int Order_ID    ) {
        this.Order_ID = Order_ID;
    }


    public int getOrder_id() {
        return Order_ID;
    }

    public void setOrder_id(int Order_ID) {
        this.Order_ID = Order_ID;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}