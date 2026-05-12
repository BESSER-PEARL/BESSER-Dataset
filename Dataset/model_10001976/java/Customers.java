





import java.util.List;
import java.util.ArrayList;

public class Customers  {

    private String NameCustomer;
    private String IdCustomer;
    private String Email;
    private String Password;



    public Customers(
        String NameCustomer,        String IdCustomer,        String Email,        String Password    ) {
        this.NameCustomer = NameCustomer;
        this.IdCustomer = IdCustomer;
        this.Email = Email;
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


}