





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Last_name;
    private String Email;
    private String Password;
    private int IDCust;
    private String Name;



    public Customer(
        String Last_name,        String Email,        String Password,        int IDCust,        String Name    ) {
        this.Last_name = Last_name;
        this.Email = Email;
        this.Password = Password;
        this.IDCust = IDCust;
        this.Name = Name;
    }


    public String getLast_name() {
        return Last_name;
    }

    public void setLast_name(String Last_name) {
        this.Last_name = Last_name;
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
    public int getIdcust() {
        return IDCust;
    }

    public void setIdcust(int IDCust) {
        this.IDCust = IDCust;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}