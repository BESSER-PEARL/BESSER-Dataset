





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String list;
    private String item;
    private int quantity;



    public Order(
        String list,        String item,        int quantity    ) {
        this.list = list;
        this.item = item;
        this.quantity = quantity;
    }


    public String getList() {
        return list;
    }

    public void setList(String list) {
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


}