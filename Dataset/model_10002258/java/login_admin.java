





import java.util.List;
import java.util.ArrayList;

public class login_admin  {

    private String password;
    private String email;





    private admin admin;


    public login_admin(
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

    public admin getAdmin() {
        return admin;
    }

    public void setAdmin(admin admin) {
        this.admin = admin;
    }

}