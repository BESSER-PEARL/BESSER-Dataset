





import java.util.List;
import java.util.ArrayList;

public class LineItem  {

    private int quantity;
    private float price;





    private Order order;


    public LineItem(
        int quantity,        float price    ) {
        this.quantity = quantity;
        this.price = price;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}