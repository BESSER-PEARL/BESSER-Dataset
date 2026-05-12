





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String login;
    private boolean isBan;
    private int id;
    private String lastname;
    private String emailAddress;
    private String password;
    private String firstname;





    private Account account;




    private ShoppingCart shoppingcart;


    public Customer(
        String login,        boolean isBan,        int id,        String lastname,        String emailAddress,        String password,        String firstname    ) {
        this.login = login;
        this.isBan = isBan;
        this.id = id;
        this.lastname = lastname;
        this.emailAddress = emailAddress;
        this.password = password;
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