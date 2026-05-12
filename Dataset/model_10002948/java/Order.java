





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int quantity;
    private String item;
    private String list;



    public Order(
        int quantity,        String item,        String list    ) {
        this.quantity = quantity;
        this.item = item;
        this.list = list;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getItem() {
        return item;
    }

    public void setItem(String item) {
        this.item = item;
    }
    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }


}