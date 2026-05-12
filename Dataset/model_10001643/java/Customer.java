





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Customer_Name;
    private int Credit_Card_Info;
    private String Address;
    private String email;



    public Customer(
        String Customer_Name,        int Credit_Card_Info,        String Address,        String email    ) {
        this.Customer_Name = Customer_Name;
        this.Credit_Card_Info = Credit_Card_Info;
        this.Address = Address;
        this.email = email;
    }


    public String getCustomer_name() {
        return Customer_Name;
    }

    public void setCustomer_name(String Customer_Name) {
        this.Customer_Name = Customer_Name;
    }
    public int getCredit_card_info() {
        return Credit_Card_Info;
    }

    public void setCredit_card_info(int Credit_Card_Info) {
        this.Credit_Card_Info = Credit_Card_Info;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}