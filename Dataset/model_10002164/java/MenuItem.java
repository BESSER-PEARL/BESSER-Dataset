





import java.util.List;
import java.util.ArrayList;

public class MenuItem  {

    private int item_price;
    private int quantity;
    private boolean available;
    private String item_description;
    private int item_Id;



    public MenuItem(
        int item_price,        int quantity,        boolean available,        String item_description,        int item_Id    ) {
        this.item_price = item_price;
        this.quantity = quantity;
        this.available = available;
        this.item_description = item_description;
        this.item_Id = item_Id;
    }


    public int getItem_price() {
        return item_price;
    }

    public void setItem_price(int item_price) {
        this.item_price = item_price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public boolean getAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }
    public String getItem_description() {
        return item_description;
    }

    public void setItem_description(String item_description) {
        this.item_description = item_description;
    }
    public int getItem_id() {
        return item_Id;
    }

    public void setItem_id(int item_Id) {
        this.item_Id = item_Id;
    }


}