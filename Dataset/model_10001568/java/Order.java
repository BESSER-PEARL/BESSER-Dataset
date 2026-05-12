





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int OrderID;
    private None items;
    private String Date;
    private None Customer;





    private Shopping_cart shopping_cart;


    public Order(
        int OrderID,        None items,        String Date,        None Customer    ) {
        this.OrderID = OrderID;
        this.items = items;
        this.Date = Date;
        this.Customer = Customer;
    }


    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public None getItems() {
        return items;
    }

    public void setItems(None items) {
        this.items = items;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public None getCustomer() {
        return Customer;
    }

    public void setCustomer(None Customer) {
        this.Customer = Customer;
    }

    public Shopping_cart getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(Shopping_cart shopping_cart) {
        this.shopping_cart = shopping_cart;
    }

}