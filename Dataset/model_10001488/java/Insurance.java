





import java.util.List;
import java.util.ArrayList;

public class Insurance  {

    private String email;
    private String password;





    private user user;


    public Insurance(
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

    public user getUser() {
        return user;
    }

    public void setUser(user user) {
        this.user = user;
    }

}