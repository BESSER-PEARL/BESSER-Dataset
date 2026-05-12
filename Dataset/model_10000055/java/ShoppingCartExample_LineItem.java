





import java.util.List;
import java.util.ArrayList;

public class ShoppingCartExample_LineItem  {

    private int quantity;
    private int price;





    private ShoppingCartExample_Order shoppingcartexample_order;


    public ShoppingCartExample_LineItem(
        int quantity,        int price    ) {
        this.quantity = quantity;
        this.price = price;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public ShoppingCartExample_Order getShoppingcartexample_order() {
        return shoppingcartexample_order;
    }

    public void setShoppingcartexample_order(ShoppingCartExample_Order shoppingcartexample_order) {
        this.shoppingcartexample_order = shoppingcartexample_order;
    }

}