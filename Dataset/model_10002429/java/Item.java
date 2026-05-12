





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private int id;
    private int quantity;
    private float price;





    private ShoppingBAsket shoppingbasket;


    public Item(
        int id,        int quantity,        float price    ) {
        this.id = id;
        this.quantity = quantity;
        this.price = price;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
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

    public ShoppingBAsket getShoppingbasket() {
        return shoppingbasket;
    }

    public void setShoppingbasket(ShoppingBAsket shoppingbasket) {
        this.shoppingbasket = shoppingbasket;
    }

}