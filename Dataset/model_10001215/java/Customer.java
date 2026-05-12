





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String name;
    private int Customer_id;



    public Customer(
        String name,        int Customer_id    ) {
        this.name = name;
        this.Customer_id = Customer_id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCustomer_id() {
        return Customer_id;
    }

    public void setCustomer_id(int Customer_id) {
        this.Customer_id = Customer_id;
    }


}