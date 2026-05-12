





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String password;
    private int id;
    private String lastname;
    private String login;
    private boolean isBan;
    private String firstname;
    private String emailAddress;





    private Account account;




    private ShoppingCart shoppingcart;


    public Customer(
        String password,        int id,        String lastname,        String login,        boolean isBan,        String firstname,        String emailAddress    ) {
        this.password = password;
        this.id = id;
        this.lastname = lastname;
        this.login = login;
        this.isBan = isBan;
        this.firstname = firstname;
        this.emailAddress = emailAddress;
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