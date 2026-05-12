





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private None state;
    private String Enter_to_Travel_Website;





    private ShoppingCart shoppingcart;




    private Customer customer;


    public WebUser(
        None state,        String Enter_to_Travel_Website    ) {
        this.state = state;
        this.Enter_to_Travel_Website = Enter_to_Travel_Website;
    }


    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }
    public String getEnter_to_travel_website() {
        return Enter_to_Travel_Website;
    }

    public void setEnter_to_travel_website(String Enter_to_Travel_Website) {
        this.Enter_to_Travel_Website = Enter_to_Travel_Website;
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