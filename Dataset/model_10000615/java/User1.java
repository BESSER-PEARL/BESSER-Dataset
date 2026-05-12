





import java.util.List;
import java.util.ArrayList;

public class User1  {

    private String email;
    private String password;



    public User1(
        String email,        String password    ) {
        this.email = email;
        this.password = password;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}