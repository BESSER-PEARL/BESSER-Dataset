





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private int OrderID;
    private int Quantity;
    private int CartID;





    private Order order;


    public Shopping_Cart(
        int OrderID,        int Quantity,        int CartID    ) {
        this.OrderID = OrderID;
        this.Quantity = Quantity;
        this.CartID = CartID;
    }


    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getCartid() {
        return CartID;
    }

    public void setCartid(int CartID) {
        this.CartID = CartID;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}