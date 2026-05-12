





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int Customer_id;
    private String name;



    public Customer(
        int Customer_id,        String name    ) {
        this.Customer_id = Customer_id;
        this.name = name;
    }


    public int getCustomer_id() {
        return Customer_id;
    }

    public void setCustomer_id(int Customer_id) {
        this.Customer_id = Customer_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}