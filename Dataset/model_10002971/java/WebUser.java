





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private None state;
    private String password;
    private String __;





    private Customer customer;




    private ShoppingCart shoppingcart;


    public WebUser(
        None state,        String password,        String __    ) {
        this.state = state;
        this.password = password;
        this.__ = __;
    }


    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String get__() {
        return __;
    }

    public void set__(String __) {
        this.__ = __;
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