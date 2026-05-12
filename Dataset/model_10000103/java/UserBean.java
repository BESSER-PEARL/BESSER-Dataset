





import java.util.List;
import java.util.ArrayList;

public class UserBean  {

    private String username;
    private String email;
    private boolean valid;
    private String registration_date;
    private String company;
    private String pass;



    public UserBean(
        String username,        String email,        boolean valid,        String registration_date,        String company,        String pass    ) {
        this.username = username;
        this.email = email;
        this.valid = valid;
        this.registration_date = registration_date;
        this.company = company;
        this.pass = pass;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public boolean getValid() {
        return valid;
    }

    public void setValid(boolean valid) {
        this.valid = valid;
    }
    public String getRegistration_date() {
        return registration_date;
    }

    public void setRegistration_date(String registration_date) {
        this.registration_date = registration_date;
    }
    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }
    public String getPass() {
        return pass;
    }

    public void setPass(String pass) {
        this.pass = pass;
    }


}