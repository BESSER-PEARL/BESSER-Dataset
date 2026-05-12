





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String cust_Id;
    private String cust_name;



    public Customer(
        String cust_Id,        String cust_name    ) {
        this.cust_Id = cust_Id;
        this.cust_name = cust_name;
    }


    public String getCust_id() {
        return cust_Id;
    }

    public void setCust_id(String cust_Id) {
        this.cust_Id = cust_Id;
    }
    public String getCust_name() {
        return cust_name;
    }

    public void setCust_name(String cust_name) {
        this.cust_name = cust_name;
    }


}