





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int customerID;
    private int phoneNumber;
    private String customerName;



    public Customer(
        int customerID,        int phoneNumber,        String customerName    ) {
        this.customerID = customerID;
        this.phoneNumber = phoneNumber;
        this.customerName = customerName;
    }


    public int getCustomerid() {
        return customerID;
    }

    public void setCustomerid(int customerID) {
        this.customerID = customerID;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }


}