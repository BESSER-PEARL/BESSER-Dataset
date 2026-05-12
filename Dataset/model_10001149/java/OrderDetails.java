





import java.util.List;
import java.util.ArrayList;

public class OrderDetails  {

    private int qty;





    private Order order;


    public OrderDetails(
        int qty    ) {
        this.qty = qty;
    }


    public int getQty() {
        return qty;
    }

    public void setQty(int qty) {
        this.qty = qty;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}