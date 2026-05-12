





import java.util.List;
import java.util.ArrayList;

public class ShoppingCartExample_Order  {

    private int id;





    private ShoppingCartExample_ShoppingCart shoppingcartexample_shoppingcart;


    public ShoppingCartExample_Order(
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

}