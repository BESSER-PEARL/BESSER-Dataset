





import java.util.List;
import java.util.ArrayList;

public class Cancelorder  {

    private int quantity;
    private String item;



    public Cancelorder(
        int quantity,        String item    ) {
        this.quantity = quantity;
        this.item = item;
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