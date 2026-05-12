





import java.util.List;
import java.util.ArrayList;

public class Shopping_cart  {

    private int Quantity;
    private int Cart_id;
    private None Customer_id;
    private None Product_Name;



    public Shopping_cart(
        int Quantity,        int Cart_id,        None Customer_id,        None Product_Name    ) {
        this.Quantity = Quantity;
        this.Cart_id = Cart_id;
        this.Customer_id = Customer_id;
        this.Product_Name = Product_Name;
    }


    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getCart_id() {
        return Cart_id;
    }

    public void setCart_id(int Cart_id) {
        this.Cart_id = Cart_id;
    }
    public None getCustomer_id() {
        return Customer_id;
    }

    public void setCustomer_id(None Customer_id) {
        this.Customer_id = Customer_id;
    }
    public None getProduct_name() {
        return Product_Name;
    }

    public void setProduct_name(None Product_Name) {
        this.Product_Name = Product_Name;
    }


}