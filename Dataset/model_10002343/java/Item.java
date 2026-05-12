





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private float price;
    private String colour;
    private String productId;





    private Account account;




    private Shopping_Cart shopping_cart;


    public Item(
        float price,        String colour,        String productId    ) {
        this.price = price;
        this.colour = colour;
        this.productId = productId;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getColour() {
        return colour;
    }

    public void setColour(String colour) {
        this.colour = colour;
    }
    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public Shopping_Cart getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(Shopping_Cart shopping_cart) {
        this.shopping_cart = shopping_cart;
    }

}