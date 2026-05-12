





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private int price;
    private int ItemID;
    private int Quantity;





    private Order order;


    public Item(
        int price,        int ItemID,        int Quantity    ) {
        this.price = price;
        this.ItemID = ItemID;
        this.Quantity = Quantity;
    }


    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public int getItemid() {
        return ItemID;
    }

    public void setItemid(int ItemID) {
        this.ItemID = ItemID;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}