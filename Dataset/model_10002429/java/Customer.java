





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int id;
    private String login;
    private String emailAddress;
    private String password;
    private String lastname;
    private String firstname;
    private boolean isBan;





    private Account account;




    private ShoppingBAsket shoppingbasket;


    public Customer(
        int id,        String login,        String emailAddress,        String password,        String lastname,        String firstname,        boolean isBan    ) {
        this.id = id;
        this.login = login;
        this.emailAddress = emailAddress;
        this.password = password;
        this.lastname = lastname;
        this.firstname = firstname;
        this.isBan = isBan;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
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
    public boolean getIsban() {
        return isBan;
    }

    public void setIsban(boolean isBan) {
        this.isBan = isBan;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public ShoppingBAsket getShoppingbasket() {
        return shoppingbasket;
    }

    public void setShoppingbasket(ShoppingBAsket shoppingbasket) {
        this.shoppingbasket = shoppingbasket;
    }

}