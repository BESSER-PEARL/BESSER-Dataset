





import java.util.List;
import java.util.ArrayList;

public class Kitchen_worker  {

    private String attribute;
    private int ID;
    private String Email;
    private String password;
    private String Name;





    private Accounnt1 accounnt1;


    public Kitchen_worker(
        String attribute,        int ID,        String Email,        String password,        String Name    ) {
        this.attribute = attribute;
        this.ID = ID;
        this.Email = Email;
        this.password = password;
        this.Name = Name;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Accounnt1 getAccounnt1() {
        return accounnt1;
    }

    public void setAccounnt1(Accounnt1 accounnt1) {
        this.accounnt1 = accounnt1;
    }

}