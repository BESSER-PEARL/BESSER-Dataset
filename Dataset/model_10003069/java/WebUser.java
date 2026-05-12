





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private None state;
    private String login;
    private String password;





    private Customer customer;




    private ShoppingCart shoppingcart;


    public WebUser(
        None state,        String login,        String password    ) {
        this.state = state;
        this.login = login;
        this.password = password;
    }


    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
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