





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private int productID;
    private String dateAdded;
    private int cartID;
    private int quantity;





    private Customer customer;


    public ShoppingCart(
        int productID,        String dateAdded,        int cartID,        int quantity    ) {
        this.productID = productID;
        this.dateAdded = dateAdded;
        this.cartID = cartID;
        this.quantity = quantity;
    }


    public int getProductid() {
        return productID;
    }

    public void setProductid(int productID) {
        this.productID = productID;
    }
    public String getDateadded() {
        return dateAdded;
    }

    public void setDateadded(String dateAdded) {
        this.dateAdded = dateAdded;
    }
    public int getCartid() {
        return cartID;
    }

    public void setCartid(int cartID) {
        this.cartID = cartID;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}