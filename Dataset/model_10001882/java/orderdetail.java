





import java.util.List;
import java.util.ArrayList;

public class Orderdetail  {

    private String productid;
    private String total;
    private String cost;
    private String orderid;
    private String quantity;





    private Order order;


    public Orderdetail(
        String productid,        String total,        String cost,        String orderid,        String quantity    ) {
        this.productid = productid;
        this.total = total;
        this.cost = cost;
        this.orderid = orderid;
        this.quantity = quantity;
    }


    public String getProductid() {
        return productid;
    }

    public void setProductid(String productid) {
        this.productid = productid;
    }
    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
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

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}