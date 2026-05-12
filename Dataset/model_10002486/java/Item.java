





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private float price;
    private int quantity;
    private int id;





    private ShoppingCart shoppingcart;


    public Item(
        float price,        int quantity,        int id    ) {
        this.price = price;
        this.quantity = quantity;
        this.id = id;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
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

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}