





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private String name;
    private float price;
    private int quantity;





    private Item item;




    private List<ShoppingCart> shoppingcarts;


    public Item(
        String name,        float price,        int quantity    ) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
        this.shoppingcarts = new ArrayList<>();
    }

    public Item(
        String name,        float price,        int quantity        ArrayList<ShoppingCart> shoppingcarts    ) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
        this.shoppingcarts = shoppingcarts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }
    public List<ShoppingCart> getShoppingcarts() {
        return shoppingcarts;
    }

    public void addShoppingcart(Shoppingcart shoppingcart) {
        this.shoppingcarts.add(shoppingcart);
    }

}