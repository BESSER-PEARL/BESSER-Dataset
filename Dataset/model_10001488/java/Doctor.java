





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String password;
    private String email;





    private user user;


    public Doctor(
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

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}