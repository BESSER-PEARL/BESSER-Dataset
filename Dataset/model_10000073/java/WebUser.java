





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private String login;
    private int userType;
    private String password;
    private None state;





    private Customer customer;




    private ShoppingCart shoppingcart;


    public WebUser(
        String login,        int userType,        String password,        None state    ) {
        this.login = login;
        this.userType = userType;
        this.password = password;
        this.state = state;
    }


    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public int getUsertype() {
        return userType;
    }

    public void setUsertype(int userType) {
        this.userType = userType;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}