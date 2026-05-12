





import java.util.List;
import java.util.ArrayList;

public class Registered_Customer  {

    private String Email;
    private String password;



    public Registered_Customer(
        String Email,        String password    ) {
        this.Email = Email;
        this.password = password;
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


}