





import java.util.List;
import java.util.ArrayList;

public class Customer_Customer  {

    private String lastname;
    private String emailAddress;
    private int id;
    private String login;
    private String password;
    private String firstname;
    private String Message;



    public Customer_Customer(
        String lastname,        String emailAddress,        int id,        String login,        String password,        String firstname,        String Message    ) {
        this.lastname = lastname;
        this.emailAddress = emailAddress;
        this.id = id;
        this.login = login;
        this.password = password;
        this.firstname = firstname;
        this.Message = Message;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getMessage() {
        return Message;
    }

    public void setMessage(String Message) {
        this.Message = Message;
    }


}