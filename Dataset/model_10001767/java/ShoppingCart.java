





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private int dateAdded;
    private int cartId;
    private int productId;
    private int quantity;





    private coustomer coustomer;


    public ShoppingCart(
        int dateAdded,        int cartId,        int productId,        int quantity    ) {
        this.dateAdded = dateAdded;
        this.cartId = cartId;
        this.productId = productId;
        this.quantity = quantity;
    }


    public int getDateadded() {
        return dateAdded;
    }

    public void setDateadded(int dateAdded) {
        this.dateAdded = dateAdded;
    }
    public int getCartid() {
        return cartId;
    }

    public void setCartid(int cartId) {
        this.cartId = cartId;
    }
    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public coustomer getCoustomer() {
        return coustomer;
    }

    public void setCoustomer(coustomer coustomer) {
        this.coustomer = coustomer;
    }

}