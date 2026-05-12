





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private int dateAdded;
    private int quantity;
    private int productId;
    private int cartId;





    private User user;


    public ShoppingCart(
        int dateAdded,        int quantity,        int productId,        int cartId    ) {
        this.dateAdded = dateAdded;
        this.quantity = quantity;
        this.productId = productId;
        this.cartId = cartId;
    }


    public int getDateadded() {
        return dateAdded;
    }

    public void setDateadded(int dateAdded) {
        this.dateAdded = dateAdded;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public int getCartid() {
        return cartId;
    }

    public void setCartid(int cartId) {
        this.cartId = cartId;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}