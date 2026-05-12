





import java.util.List;
import java.util.ArrayList;

public class OrderItem  {

    private String OrderId;
    private String ItemId;
    private String Price;
    private String Name;
    private int Amount;



    public OrderItem(
        String OrderId,        String ItemId,        String Price,        String Name,        int Amount    ) {
        this.OrderId = OrderId;
        this.ItemId = ItemId;
        this.Price = Price;
        this.Name = Name;
        this.Amount = Amount;
    }


    public String getOrderid() {
        return OrderId;
    }

    public void setOrderid(String OrderId) {
        this.OrderId = OrderId;
    }
    public String getItemid() {
        return ItemId;
    }

    public void setItemid(String ItemId) {
        this.ItemId = ItemId;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getAmount() {
        return Amount;
    }

    public void setAmount(int Amount) {
        this.Amount = Amount;
    }


}