





import java.util.List;
import java.util.ArrayList;

public class ShoppingCartExample_Account  {

    private int id;





    private ShoppingCartExample_ShoppingCart shoppingcartexample_shoppingcart;




    private ShoppingCartExample_Customer shoppingcartexample_customer;


    public ShoppingCartExample_Account(
        int id    ) {
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public ShoppingCartExample_ShoppingCart getShoppingcartexample_shoppingcart() {
        return shoppingcartexample_shoppingcart;
    }

    public void setShoppingcartexample_shoppingcart(ShoppingCartExample_ShoppingCart shoppingcartexample_shoppingcart) {
        this.shoppingcartexample_shoppingcart = shoppingcartexample_shoppingcart;
    }
    public ShoppingCartExample_Customer getShoppingcartexample_customer() {
        return shoppingcartexample_customer;
    }

    public void setShoppingcartexample_customer(ShoppingCartExample_Customer shoppingcartexample_customer) {
        this.shoppingcartexample_customer = shoppingcartexample_customer;
    }

}