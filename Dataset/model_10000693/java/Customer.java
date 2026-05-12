





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String login;
    private String lastname;
    private String emailAddress;
    private String password;
    private String firstname;
    private boolean isBan;
    private int id;





    private ShoppingCart shoppingcart;




    private Account account;


    public Customer(
        String login,        String lastname,        String emailAddress,        String password,        String firstname,        boolean isBan,        int id    ) {
        this.login = login;
        this.lastname = lastname;
        this.emailAddress = emailAddress;
        this.password = password;
        this.firstname = firstname;
        this.isBan = isBan;
        this.id = id;
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
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
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
    public boolean getIsban() {
        return isBan;
    }

    public void setIsban(boolean isBan) {
        this.isBan = isBan;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}