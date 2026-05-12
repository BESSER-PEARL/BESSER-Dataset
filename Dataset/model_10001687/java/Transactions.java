





import java.util.List;
import java.util.ArrayList;

public class Transactions  {

    private String Customer;
    private String Order;



    public Transactions(
        String Customer,        String Order    ) {
        this.Customer = Customer;
        this.Order = Order;
    }


    public String getCustomer() {
        return Customer;
    }

    public void setCustomer(String Customer) {
        this.Customer = Customer;
    }
    public String getOrder() {
        return Order;
    }

    public void setOrder(String Order) {
        this.Order = Order;
    }


}