





import java.util.List;
import java.util.ArrayList;

public class Customer1  {

    private String attribute;
    private String ID;
    private String Password;
    private String Name;
    private String Email;



    public Customer1(
        String attribute,        String ID,        String Password,        String Name,        String Email    ) {
        this.attribute = attribute;
        this.ID = ID;
        this.Password = Password;
        this.Name = Name;
        this.Email = Email;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}