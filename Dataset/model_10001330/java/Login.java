





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String Password;
    private String Email;



    public Login(
        String Password,        String Email    ) {
        this.Password = Password;
        this.Email = Email;
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


}