





import java.util.List;
import java.util.ArrayList;

public class ShippingCart  {

    private int dateAdded;
    private int productID;
    private int quantity;
    private int cartID;





    private CustomerInfo customerinfo;


    public ShippingCart(
        int dateAdded,        int productID,        int quantity,        int cartID    ) {
        this.dateAdded = dateAdded;
        this.productID = productID;
        this.quantity = quantity;
        this.cartID = cartID;
    }


    public int getDateadded() {
        return dateAdded;
    }

    public void setDateadded(int dateAdded) {
        this.dateAdded = dateAdded;
    }
    public int getProductid() {
        return productID;
    }

    public void setProductid(int productID) {
        this.productID = productID;
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

    public CustomerInfo getCustomerinfo() {
        return customerinfo;
    }

    public void setCustomerinfo(CustomerInfo customerinfo) {
        this.customerinfo = customerinfo;
    }

}