





import java.util.List;
import java.util.ArrayList;

public class RadixClient  {

    private String password;
    private None state;
    private String populate;





    private ShoppingCart shoppingcart;


    public RadixClient(
        String password,        None state,        String populate    ) {
        this.password = password;
        this.state = state;
        this.populate = populate;
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
    public String getPopulate() {
        return populate;
    }

    public void setPopulate(String populate) {
        this.populate = populate;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}