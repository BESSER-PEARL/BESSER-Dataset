





import java.util.List;
import java.util.ArrayList;

public class Customer_Support  {

    private String Password;
    private int ID;
    private String Email;





    private Customer customer;


    public Customer_Support(
        String Password,        int ID,        String Email    ) {
        this.Password = Password;
        this.ID = ID;
        this.Email = Email;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}