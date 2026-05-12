





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private boolean isBan;
    private String firstname;
    private String emailAddress;
    private String login;
    private int id;
    private String lastname;
    private String password;





    private ShoppingCart shoppingcart;




    private Account account;


    public Customer(
        boolean isBan,        String firstname,        String emailAddress,        String login,        int id,        String lastname,        String password    ) {
        this.isBan = isBan;
        this.firstname = firstname;
        this.emailAddress = emailAddress;
        this.login = login;
        this.id = id;
        this.lastname = lastname;
        this.password = password;
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