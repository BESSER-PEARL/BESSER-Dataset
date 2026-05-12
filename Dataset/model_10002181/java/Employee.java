





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String password;
    private int ID;
    private String Name;
    private String Email;
    private String attribute;



    public Employee(
        String password,        int ID,        String Name,        String Email,        String attribute    ) {
        this.password = password;
        this.ID = ID;
        this.Name = Name;
        this.Email = Email;
        this.attribute = attribute;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
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
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}