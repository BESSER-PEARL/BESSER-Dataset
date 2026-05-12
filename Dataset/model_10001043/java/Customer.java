





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String login;
    private String firstname;
    private boolean isBan;
    private String lastname;
    private int id;
    private String emailAddress;
    private String password;





    private ShoppingCart shoppingcart;




    private Account account;


    public Customer(
        String login,        String firstname,        boolean isBan,        String lastname,        int id,        String emailAddress,        String password    ) {
        this.login = login;
        this.firstname = firstname;
        this.isBan = isBan;
        this.lastname = lastname;
        this.id = id;
        this.emailAddress = emailAddress;
        this.password = password;
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