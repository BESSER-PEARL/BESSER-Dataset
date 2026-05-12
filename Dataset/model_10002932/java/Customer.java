





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int id;
    private String lastname;
    private String login;
    private String password;
    private String emailAddress;
    private String firstname;
    private boolean isBan;





    private ShoppingCart shoppingcart;




    private Account account;


    public Customer(
        int id,        String lastname,        String login,        String password,        String emailAddress,        String firstname,        boolean isBan    ) {
        this.id = id;
        this.lastname = lastname;
        this.login = login;
        this.password = password;
        this.emailAddress = emailAddress;
        this.firstname = firstname;
        this.isBan = isBan;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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