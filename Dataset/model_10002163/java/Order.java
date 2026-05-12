





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String Date;





    private Order_Status order_status;




    private Customer customer;


    public Order(
        String Date    ) {
        this.Date = Date;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }

    public Order_Status getOrder_status() {
        return order_status;
    }

    public void setOrder_status(Order_Status order_status) {
        this.order_status = order_status;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}