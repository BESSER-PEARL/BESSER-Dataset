





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String password;
    private String login;





    private ShoppingCart shoppingcart;


    public User(
        String password,        String login    ) {
        this.password = password;
        this.login = login;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}