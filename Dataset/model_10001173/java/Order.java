





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String item;
    private String list;
    private int quantity;



    public Order(
        String item,        String list,        int quantity    ) {
        this.item = item;
        this.list = list;
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
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}