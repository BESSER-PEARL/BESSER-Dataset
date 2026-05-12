





import java.util.List;
import java.util.ArrayList;

public class Employee1  {

    private String ID;
    private String Password;
    private String Email;
    private String Name;
    private String attribute;



    public Employee1(
        String ID,        String Password,        String Email,        String Name,        String attribute    ) {
        this.ID = ID;
        this.Password = Password;
        this.Email = Email;
        this.Name = Name;
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
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}