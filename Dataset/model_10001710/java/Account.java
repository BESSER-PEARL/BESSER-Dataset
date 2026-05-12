





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String open;
    private String billing_address;
    private String id;





    private Customer customer;


    public Account(
        String open,        String billing_address,        String id    ) {
        this.open = open;
        this.billing_address = billing_address;
        this.id = id;
    }


    public String getOpen() {
        return open;
    }

    public void setOpen(String open) {
        this.open = open;
    }
    public String getBilling_address() {
        return billing_address;
    }

    public void setBilling_address(String billing_address) {
        this.billing_address = billing_address;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}