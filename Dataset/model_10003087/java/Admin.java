





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String password;
    private String email;



    public Admin(
        String password,        String email    ) {
        this.password = password;
        this.email = email;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}