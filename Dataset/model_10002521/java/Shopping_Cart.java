





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private String dateAdded;
    private int quantity;
    private String cartId;





    private Customer customer;


    public Shopping_Cart(
        String dateAdded,        int quantity,        String cartId    ) {
        this.dateAdded = dateAdded;
        this.quantity = quantity;
        this.cartId = cartId;
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
    public String getCartid() {
        return cartId;
    }

    public void setCartid(String cartId) {
        this.cartId = cartId;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}