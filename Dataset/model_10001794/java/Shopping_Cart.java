





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private int productId;
    private int dateAdded;
    private int Quantity;
    private int CartId;



    public Shopping_Cart(
        int productId,        int dateAdded,        int Quantity,        int CartId    ) {
        this.productId = productId;
        this.dateAdded = dateAdded;
        this.Quantity = Quantity;
        this.CartId = CartId;
    }


    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public int getDateadded() {
        return dateAdded;
    }

    public void setDateadded(int dateAdded) {
        this.dateAdded = dateAdded;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getCartid() {
        return CartId;
    }

    public void setCartid(int CartId) {
        this.CartId = CartId;
    }


}