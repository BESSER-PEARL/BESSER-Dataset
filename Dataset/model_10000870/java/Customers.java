





import java.util.List;
import java.util.ArrayList;

public class Customers  {

    private String Email;
    private String Password;
    private String NameCustomer;
    private String IdCustomer;



    public Customers(
        String Email,        String Password,        String NameCustomer,        String IdCustomer    ) {
        this.Email = Email;
        this.Password = Password;
        this.NameCustomer = NameCustomer;
        this.IdCustomer = IdCustomer;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getNamecustomer() {
        return NameCustomer;
    }

    public void setNamecustomer(String NameCustomer) {
        this.NameCustomer = NameCustomer;
    }
    public String getIdcustomer() {
        return IdCustomer;
    }

    public void setIdcustomer(String IdCustomer) {
        this.IdCustomer = IdCustomer;
    }


}