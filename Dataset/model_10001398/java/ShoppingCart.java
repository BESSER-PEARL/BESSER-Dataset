





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private int dateAdded;
    private int cartId;
    private int quantity;
    private int productId;





    private coustomer coustomer;


    public ShoppingCart(
        int dateAdded,        int cartId,        int quantity,        int productId    ) {
        this.dateAdded = dateAdded;
        this.cartId = cartId;
        this.quantity = quantity;
        this.productId = productId;
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

    public coustomer getCoustomer() {
        return coustomer;
    }

    public void setCoustomer(coustomer coustomer) {
        this.coustomer = coustomer;
    }

}