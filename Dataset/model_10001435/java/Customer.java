





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Password;
    private String Full_Name;
    private int CustomerId;
    private String Delivery_address;
    private String Email_Address;



    public Customer(
        String Password,        String Full_Name,        int CustomerId,        String Delivery_address,        String Email_Address    ) {
        this.Password = Password;
        this.Full_Name = Full_Name;
        this.CustomerId = CustomerId;
        this.Delivery_address = Delivery_address;
        this.Email_Address = Email_Address;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getFull_name() {
        return Full_Name;
    }

    public void setFull_name(String Full_Name) {
        this.Full_Name = Full_Name;
    }
    public int getCustomerid() {
        return CustomerId;
    }

    public void setCustomerid(int CustomerId) {
        this.CustomerId = CustomerId;
    }
    public String getDelivery_address() {
        return Delivery_address;
    }

    public void setDelivery_address(String Delivery_address) {
        this.Delivery_address = Delivery_address;
    }
    public String getEmail_address() {
        return Email_Address;
    }

    public void setEmail_address(String Email_Address) {
        this.Email_Address = Email_Address;
    }


}