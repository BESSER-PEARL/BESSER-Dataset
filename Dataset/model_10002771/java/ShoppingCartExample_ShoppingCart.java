




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCartExample_ShoppingCart  {

    private LocalDate creationDate;





    private List<ShoppingCartExample_Order> shoppingcartexample_orders;


    public ShoppingCartExample_ShoppingCart(
        LocalDate creationDate    ) {
        this.creationDate = creationDate;
        this.shoppingcartexample_orders = new ArrayList<>();
    }

    public ShoppingCartExample_ShoppingCart(
        LocalDate creationDate        ArrayList<ShoppingCartExample_Order> shoppingcartexample_orders    ) {
        this.creationDate = creationDate;
        this.shoppingcartexample_orders = shoppingcartexample_orders;
    }

    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public List<ShoppingCartExample_Order> getShoppingcartexample_orders() {
        return shoppingcartexample_orders;
    }

    public void addShoppingcartexample_order(Shoppingcartexample_order shoppingcartexample_order) {
        this.shoppingcartexample_orders.add(shoppingcartexample_order);
    }

}