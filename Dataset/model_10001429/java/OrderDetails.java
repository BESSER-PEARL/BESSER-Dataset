





import java.util.List;
import java.util.ArrayList;

public class OrderDetails  {

    private int quantity;
    private int order_id;
    private int product_id;
    private String product_name;





    private Orders orders;


    public OrderDetails(
        int quantity,        int order_id,        int product_id,        String product_name    ) {
        this.quantity = quantity;
        this.order_id = order_id;
        this.product_id = product_id;
        this.product_name = product_name;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getOrder_id() {
        return order_id;
    }

    public void setOrder_id(int order_id) {
        this.order_id = order_id;
    }
    public int getProduct_id() {
        return product_id;
    }

    public void setProduct_id(int product_id) {
        this.product_id = product_id;
    }
    public String getProduct_name() {
        return product_name;
    }

    public void setProduct_name(String product_name) {
        this.product_name = product_name;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

}