





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String login;
    private int id;
    private String firstname;
    private String emailAddress;
    private String lastname;
    private boolean isBan;
    private String password;



    public Customer(
        String login,        int id,        String firstname,        String emailAddress,        String lastname,        boolean isBan,        String password    ) {
        this.login = login;
        this.id = id;
        this.firstname = firstname;
        this.emailAddress = emailAddress;
        this.lastname = lastname;
        this.isBan = isBan;
        this.password = password;
    }


    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public boolean getIsban() {
        return isBan;
    }

    public void setIsban(boolean isBan) {
        this.isBan = isBan;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}