





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_Shopping_Cart_Item  {

    private int Price;
    private String Quantity;





    private Online_Shopping_Shopping_Cart online_shopping_shopping_cart;


    public Online_Shopping_Shopping_Cart_Item(
        int Price,        String Quantity    ) {
        this.Price = Price;
        this.Quantity = Quantity;
    }


    public int getPrice() {
        return Price;
    }

    public void setPrice(int Price) {
        this.Price = Price;
    }
    public String getQuantity() {
        return Quantity;
    }

    public void setQuantity(String Quantity) {
        this.Quantity = Quantity;
    }

    public Online_Shopping_Shopping_Cart getOnline_shopping_shopping_cart() {
        return online_shopping_shopping_cart;
    }

    public void setOnline_shopping_shopping_cart(Online_Shopping_Shopping_Cart online_shopping_shopping_cart) {
        this.online_shopping_shopping_cart = online_shopping_shopping_cart;
    }

}