





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String login;
    private String firstname;
    private int id;
    private String emailAddress;
    private String lastname;
    private String password;
    private boolean isBan;





    private ShoppingCart shoppingcart;




    private Account account;


    public Customer(
        String login,        String firstname,        int id,        String emailAddress,        String lastname,        String password,        boolean isBan    ) {
        this.login = login;
        this.firstname = firstname;
        this.id = id;
        this.emailAddress = emailAddress;
        this.lastname = lastname;
        this.password = password;
        this.isBan = isBan;
    }


    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public boolean getIsban() {
        return isBan;
    }

    public void setIsban(boolean isBan) {
        this.isBan = isBan;
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