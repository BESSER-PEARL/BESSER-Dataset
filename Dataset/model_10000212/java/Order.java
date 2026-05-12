





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String item;
    private int quantity;
    private String list;



    public Order(
        String item,        int quantity,        String list    ) {
        this.item = item;
        this.quantity = quantity;
        this.list = list;
    }


    public String getItem() {
        return item;
    }

    public void setItem(String item) {
        this.item = item;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }


}