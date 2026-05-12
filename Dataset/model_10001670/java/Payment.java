





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int Date;
    private String Payment_ID;





    private Customer customer;


    public Payment(
        int Date,        String Payment_ID    ) {
        this.Date = Date;
        this.Payment_ID = Payment_ID;
    }


    public int getDate() {
        return Date;
    }

    public void setDate(int Date) {
        this.Date = Date;
    }
    public String getPayment_id() {
        return Payment_ID;
    }

    public void setPayment_id(String Payment_ID) {
        this.Payment_ID = Payment_ID;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}