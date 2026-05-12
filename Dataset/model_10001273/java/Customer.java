





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String lastname;
    private boolean isBan;
    private String emailAddress;
    private String login;
    private String password;
    private String firstname;
    private int id;





    private Account account;




    private ShoppingCart shoppingcart;


    public Customer(
        String lastname,        boolean isBan,        String emailAddress,        String login,        String password,        String firstname,        int id    ) {
        this.lastname = lastname;
        this.isBan = isBan;
        this.emailAddress = emailAddress;
        this.login = login;
        this.password = password;
        this.firstname = firstname;
        this.id = id;
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
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
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