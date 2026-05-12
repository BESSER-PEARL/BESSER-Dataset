





import java.util.List;
import java.util.ArrayList;

public class ShoppingCartExample_LineItem  {

    private int price;
    private int quantity;





    private ShoppingCartExample_Order shoppingcartexample_order;


    public ShoppingCartExample_LineItem(
        int price,        int quantity    ) {
        this.price = price;
        this.quantity = quantity;
    }


    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public ShoppingCartExample_Order getShoppingcartexample_order() {
        return shoppingcartexample_order;
    }

    public void setShoppingcartexample_order(ShoppingCartExample_Order shoppingcartexample_order) {
        this.shoppingcartexample_order = shoppingcartexample_order;
    }

}