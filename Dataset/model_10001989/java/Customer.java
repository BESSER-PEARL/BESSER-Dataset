





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Name;
    private int Customer_ID;



    public Customer(
        String Name,        int Customer_ID    ) {
        this.Name = Name;
        this.Customer_ID = Customer_ID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getCustomer_id() {
        return Customer_ID;
    }

    public void setCustomer_id(int Customer_ID) {
        this.Customer_ID = Customer_ID;
    }


}