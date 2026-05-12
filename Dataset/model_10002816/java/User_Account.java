





import java.util.List;
import java.util.ArrayList;

public class User_Account  {

    private String password;
    private String telephone;
    private String email;
    private String full_name;



    public User_Account(
        String password,        String telephone,        String email,        String full_name    ) {
        this.password = password;
        this.telephone = telephone;
        this.email = email;
        this.full_name = full_name;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getFull_name() {
        return full_name;
    }

    public void setFull_name(String full_name) {
        this.full_name = full_name;
    }


}