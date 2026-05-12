





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private String cartId;





    private Order order;


    public Shopping_Cart(
        String cartId    ) {
        this.cartId = cartId;
    }


    public String getCartid() {
        return cartId;
    }

    public void setCartid(String cartId) {
        this.cartId = cartId;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}