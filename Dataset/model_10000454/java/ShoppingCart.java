





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private int CartID;
    private int DateAdded;
    private int ProductID;
    private int Quantity;





    private Customer customer;


    public ShoppingCart(
        int CartID,        int DateAdded,        int ProductID,        int Quantity    ) {
        this.CartID = CartID;
        this.DateAdded = DateAdded;
        this.ProductID = ProductID;
        this.Quantity = Quantity;
    }


    public int getCartid() {
        return CartID;
    }

    public void setCartid(int CartID) {
        this.CartID = CartID;
    }
    public int getDateadded() {
        return DateAdded;
    }

    public void setDateadded(int DateAdded) {
        this.DateAdded = DateAdded;
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

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}