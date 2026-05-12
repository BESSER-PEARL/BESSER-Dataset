





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String password;
    private String firstname;
    private boolean isBan;
    private String lastname;
    private String login;
    private String emailAddress;
    private int id;





    private Account account;




    private ShoppingCart shoppingcart;


    public Customer(
        String password,        String firstname,        boolean isBan,        String lastname,        String login,        String emailAddress,        int id    ) {
        this.password = password;
        this.firstname = firstname;
        this.isBan = isBan;
        this.lastname = lastname;
        this.login = login;
        this.emailAddress = emailAddress;
        this.id = id;
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
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
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

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}