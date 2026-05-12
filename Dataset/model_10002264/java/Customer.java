





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String emailAddress;
    private boolean isBan;
    private String login;
    private String lastname;
    private String firstname;
    private int id;
    private String password;





    private ShoppingCart shoppingcart;




    private Account account;


    public Customer(
        String emailAddress,        boolean isBan,        String login,        String lastname,        String firstname,        int id,        String password    ) {
        this.emailAddress = emailAddress;
        this.isBan = isBan;
        this.login = login;
        this.lastname = lastname;
        this.firstname = firstname;
        this.id = id;
        this.password = password;
    }


    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
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