





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private int quantity;
    private int dateAdded;
    private String Item;
    private String GetTotalPrice;





    private Item item;


    public ShoppingCart(
        int quantity,        int dateAdded,        String Item,        String GetTotalPrice    ) {
        this.quantity = quantity;
        this.dateAdded = dateAdded;
        this.Item = Item;
        this.GetTotalPrice = GetTotalPrice;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getDateadded() {
        return dateAdded;
    }

    public void setDateadded(int dateAdded) {
        this.dateAdded = dateAdded;
    }
    public String getItem() {
        return Item;
    }

    public void setItem(String Item) {
        this.Item = Item;
    }
    public String getGettotalprice() {
        return GetTotalPrice;
    }

    public void setGettotalprice(String GetTotalPrice) {
        this.GetTotalPrice = GetTotalPrice;
    }

    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }

}