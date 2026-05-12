





import java.util.List;
import java.util.ArrayList;

public class Registered_Customer  {

    private String password;
    private String Email;



    public Registered_Customer(
        String password,        String Email    ) {
        this.password = password;
        this.Email = Email;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}