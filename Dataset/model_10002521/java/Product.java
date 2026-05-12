





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int quantity;
    private int price;
    private String name;
    private String productID;





    private Shopping_Cart shopping_cart;


    public Product(
        int quantity,        int price,        String name,        String productID    ) {
        this.quantity = quantity;
        this.price = price;
        this.name = name;
        this.productID = productID;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProductid() {
        return productID;
    }

    public void setProductid(String productID) {
        this.productID = productID;
    }

    public Shopping_Cart getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(Shopping_Cart shopping_cart) {
        this.shopping_cart = shopping_cart;
    }

}