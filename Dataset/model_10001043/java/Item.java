





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private int quantity;
    private int id;
    private float price;





    private ShoppingCart shoppingcart;


    public Item(
        int quantity,        int id,        float price    ) {
        this.quantity = quantity;
        this.id = id;
        this.price = price;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}