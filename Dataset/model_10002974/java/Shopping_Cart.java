





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private int Quantity;
    private int productId;
    private int CartId;
    private int dateAdded;





    private Client client;


    public Shopping_Cart(
        int Quantity,        int productId,        int CartId,        int dateAdded    ) {
        this.Quantity = Quantity;
        this.productId = productId;
        this.CartId = CartId;
        this.dateAdded = dateAdded;
    }


    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public int getCartid() {
        return CartId;
    }

    public void setCartid(int CartId) {
        this.CartId = CartId;
    }
    public int getDateadded() {
        return dateAdded;
    }

    public void setDateadded(int dateAdded) {
        this.dateAdded = dateAdded;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

}