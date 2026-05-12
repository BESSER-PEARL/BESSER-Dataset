





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private int CartID;
    private int ProductID;
    private int Quantity;
    private int DateAdded;





    private Customer customer;


    public ShoppingCart(
        int CartID,        int ProductID,        int Quantity,        int DateAdded    ) {
        this.CartID = CartID;
        this.ProductID = ProductID;
        this.Quantity = Quantity;
        this.DateAdded = DateAdded;
    }


    public int getCartid() {
        return CartID;
    }

    public void setCartid(int CartID) {
        this.CartID = CartID;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getDateadded() {
        return DateAdded;
    }

    public void setDateadded(int DateAdded) {
        this.DateAdded = DateAdded;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}