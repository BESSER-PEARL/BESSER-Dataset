





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private String Date;





    private Customer customer;


    public Shopping_Cart(
        String Date    ) {
        this.Date = Date;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}