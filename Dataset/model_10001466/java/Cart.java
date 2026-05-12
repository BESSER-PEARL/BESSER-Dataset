





import java.util.List;
import java.util.ArrayList;

public class Cart  {

    private String date;
    private String ProductID;
    private int Quantity;
    private int cartID;





    private Customer customer;


    public Cart(
        String date,        String ProductID,        int Quantity,        int cartID    ) {
        this.date = date;
        this.ProductID = ProductID;
        this.Quantity = Quantity;
        this.cartID = cartID;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getProductid() {
        return ProductID;
    }

    public void setProductid(String ProductID) {
        this.ProductID = ProductID;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getCartid() {
        return cartID;
    }

    public void setCartid(int cartID) {
        this.cartID = cartID;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}