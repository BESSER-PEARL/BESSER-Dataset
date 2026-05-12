





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String list;
    private int quantity;
    private String item;



    public Order(
        String list,        int quantity,        String item    ) {
        this.list = list;
        this.quantity = quantity;
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
    public String getItem() {
        return item;
    }

    public void setItem(String item) {
        this.item = item;
    }


}