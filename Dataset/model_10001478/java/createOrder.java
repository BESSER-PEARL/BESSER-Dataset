





import java.util.List;
import java.util.ArrayList;

public class createOrder  {

    private String orderedItems;





    private Customer customer;


    public createOrder(
        String orderedItems    ) {
        this.orderedItems = orderedItems;
    }


    public String getOrdereditems() {
        return orderedItems;
    }

    public void setOrdereditems(String orderedItems) {
        this.orderedItems = orderedItems;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}