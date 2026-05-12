





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int id;
    private String password;
    private String login;
    private String lastname;
    private boolean isBan;
    private String firstname;
    private String emailAddress;





    private Account account;


    public Customer(
        int id,        String password,        String login,        String lastname,        boolean isBan,        String firstname,        String emailAddress    ) {
        this.id = id;
        this.password = password;
        this.login = login;
        this.lastname = lastname;
        this.isBan = isBan;
        this.firstname = firstname;
        this.emailAddress = emailAddress;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
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

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}