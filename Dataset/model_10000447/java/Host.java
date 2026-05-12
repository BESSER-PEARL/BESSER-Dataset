





import java.util.List;
import java.util.ArrayList;

public class Host  {

    private String shift;
    private String ID;





    private Customer customer;


    public Host(
        String shift,        String ID    ) {
        this.shift = shift;
        this.ID = ID;
    }


    public String getShift() {
        return shift;
    }

    public void setShift(String shift) {
        this.shift = shift;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}