





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private String productId;
    private float price;
    private String size;
    private String colour;





    private Account account;




    private Shopping_Cart shopping_cart;


    public Item(
        String productId,        float price,        String size,        String colour    ) {
        this.productId = productId;
        this.price = price;
        this.size = size;
        this.colour = colour;
    }


    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getColour() {
        return colour;
    }

    public void setColour(String colour) {
        this.colour = colour;
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