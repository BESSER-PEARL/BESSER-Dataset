





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private int quantity;
    private float price;
    private int id;





    private ShoppingCart shoppingcart;


    public Item(
        int quantity,        float price,        int id    ) {
        this.quantity = quantity;
        this.price = price;
        this.id = id;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
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