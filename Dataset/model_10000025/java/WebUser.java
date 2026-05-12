





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private None state;





    private ShoppingCart shoppingcart;




    private Customer customer;


    public WebUser(
        None state    ) {
        this.state = state;
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
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}