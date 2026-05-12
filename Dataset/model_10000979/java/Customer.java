





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int id;
    private String firstname;
    private String emailAddress;
    private String password;
    private boolean isBan;
    private String login;
    private String lastname;





    private ShoppingCart shoppingcart;




    private Account account;


    public Customer(
        int id,        String firstname,        String emailAddress,        String password,        boolean isBan,        String login,        String lastname    ) {
        this.id = id;
        this.firstname = firstname;
        this.emailAddress = emailAddress;
        this.password = password;
        this.isBan = isBan;
        this.login = login;
        this.lastname = lastname;
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