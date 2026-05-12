





import java.util.List;
import java.util.ArrayList;

public class Orderdetail  {

    private String orderid;
    private String quantity;
    private String productid;
    private String cost;
    private String total;





    private Order order;


    public Orderdetail(
        String orderid,        String quantity,        String productid,        String cost,        String total    ) {
        this.orderid = orderid;
        this.quantity = quantity;
        this.productid = productid;
        this.cost = cost;
        this.total = total;
    }


    public String getOrderid() {
        return orderid;
    }

    public void setOrderid(String orderid) {
        this.orderid = orderid;
    }
    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getProductid() {
        return productid;
    }

    public void setProductid(String productid) {
        this.productid = productid;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }
    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}