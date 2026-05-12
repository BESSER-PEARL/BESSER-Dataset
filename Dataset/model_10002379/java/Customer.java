





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String emailAddress;
    private String firstname;
    private String login;
    private boolean isBan;
    private String lastname;
    private String password;
    private int id;





    private ShoppingCart shoppingcart;




    private Account account;


    public Customer(
        String emailAddress,        String firstname,        String login,        boolean isBan,        String lastname,        String password,        int id    ) {
        this.emailAddress = emailAddress;
        this.firstname = firstname;
        this.login = login;
        this.isBan = isBan;
        this.lastname = lastname;
        this.password = password;
        this.id = id;
    }


    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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