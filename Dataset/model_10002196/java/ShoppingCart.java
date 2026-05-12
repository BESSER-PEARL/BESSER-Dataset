





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private String dateAdded;
    private int quantity;
    private int cartID;
    private int productID;





    private Customer customer;


    public ShoppingCart(
        String dateAdded,        int quantity,        int cartID,        int productID    ) {
        this.dateAdded = dateAdded;
        this.quantity = quantity;
        this.cartID = cartID;
        this.productID = productID;
    }


    public String getDateadded() {
        return dateAdded;
    }

    public void setDateadded(String dateAdded) {
        this.dateAdded = dateAdded;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getCartid() {
        return cartID;
    }

    public void setCartid(int cartID) {
        this.cartID = cartID;
    }
    public int getProductid() {
        return productID;
    }

    public void setProductid(int productID) {
        this.productID = productID;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}