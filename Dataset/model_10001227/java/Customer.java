





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Password;
    private String Name;



    public Customer(
        String Password,        String Name    ) {
        this.Password = Password;
        this.Name = Name;
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


}