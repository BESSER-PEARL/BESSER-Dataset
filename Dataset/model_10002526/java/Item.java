





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private int Quantity;
    private int ItemID;
    private int price;





    private Order order;


    public Item(
        int Quantity,        int ItemID,        int price    ) {
        this.Quantity = Quantity;
        this.ItemID = ItemID;
        this.price = price;
    }


    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public int getItemid() {
        return ItemID;
    }

    public void setItemid(int ItemID) {
        this.ItemID = ItemID;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}