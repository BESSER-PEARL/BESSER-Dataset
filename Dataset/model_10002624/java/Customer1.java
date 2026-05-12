





import java.util.List;
import java.util.ArrayList;

public class Customer1  {

    private String Customer_Name;
    private String S;



    public Customer1(
        String Customer_Name,        String S    ) {
        this.Customer_Name = Customer_Name;
        this.S = S;
    }


    public String getCustomer_name() {
        return Customer_Name;
    }

    public void setCustomer_name(String Customer_Name) {
        this.Customer_Name = Customer_Name;
    }
    public String getS() {
        return S;
    }

    public void setS(String S) {
        this.S = S;
    }


}