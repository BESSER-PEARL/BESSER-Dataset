





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private int Cart_id;
    private int Quantity;
    private int Product_id;





    private Customer customer;


    public Shopping_Cart(
        int Cart_id,        int Quantity,        int Product_id    ) {
        this.Cart_id = Cart_id;
        this.Quantity = Quantity;
        this.Product_id = Product_id;
    }


    public int getCart_id() {
        return Cart_id;
    }

    public void setCart_id(int Cart_id) {
        this.Cart_id = Cart_id;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getProduct_id() {
        return Product_id;
    }

    public void setProduct_id(int Product_id) {
        this.Product_id = Product_id;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}