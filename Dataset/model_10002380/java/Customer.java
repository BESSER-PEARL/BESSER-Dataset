





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int Credit_Card_Info;
    private String Address;
    private String Customer_Name;
    private String email;



    public Customer(
        int Credit_Card_Info,        String Address,        String Customer_Name,        String email    ) {
        this.Credit_Card_Info = Credit_Card_Info;
        this.Address = Address;
        this.Customer_Name = Customer_Name;
        this.email = email;
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
    public String getCustomer_name() {
        return Customer_Name;
    }

    public void setCustomer_name(String Customer_Name) {
        this.Customer_Name = Customer_Name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}