





import java.util.List;
import java.util.ArrayList;

public class Visitor  {






    private Customer customer;




    private ShoppingCart shoppingcart;


    public Visitor(
    ) {
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