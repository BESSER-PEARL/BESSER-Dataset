





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private String login;
    private String password;
    private None state;





    private ShoppingCart shoppingcart;


    public WebUser(
        String login,        String password,        None state    ) {
        this.login = login;
        this.password = password;
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
    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}