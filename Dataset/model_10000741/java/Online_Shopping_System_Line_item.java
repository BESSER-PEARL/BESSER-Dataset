





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Line_item  {

    private int quantity;
    private String price;





    private Online_Shopping_System_Order online_shopping_system_order;




    private Online_Shopping_System_Shopping_Cart online_shopping_system_shopping_cart;


    public Online_Shopping_System_Line_item(
        int quantity,        String price    ) {
        this.quantity = quantity;
        this.price = price;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public Online_Shopping_System_Order getOnline_shopping_system_order() {
        return online_shopping_system_order;
    }

    public void setOnline_shopping_system_order(Online_Shopping_System_Order online_shopping_system_order) {
        this.online_shopping_system_order = online_shopping_system_order;
    }
    public Online_Shopping_System_Shopping_Cart getOnline_shopping_system_shopping_cart() {
        return online_shopping_system_shopping_cart;
    }

    public void setOnline_shopping_system_shopping_cart(Online_Shopping_System_Shopping_Cart online_shopping_system_shopping_cart) {
        this.online_shopping_system_shopping_cart = online_shopping_system_shopping_cart;
    }

}