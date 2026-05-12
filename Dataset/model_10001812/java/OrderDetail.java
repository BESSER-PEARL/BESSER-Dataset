





import java.util.List;
import java.util.ArrayList;

public class OrderDetail  {

    private int orderId;
    private String subTotal;
    private int quantity;
    private int productId;
    private String unitCost;
    private String productName;





    private Order order;


    public OrderDetail(
        int orderId,        String subTotal,        int quantity,        int productId,        String unitCost,        String productName    ) {
        this.orderId = orderId;
        this.subTotal = subTotal;
        this.quantity = quantity;
        this.productId = productId;
        this.unitCost = unitCost;
        this.productName = productName;
    }


    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }
    public String getSubtotal() {
        return subTotal;
    }

    public void setSubtotal(String subTotal) {
        this.subTotal = subTotal;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public String getUnitcost() {
        return unitCost;
    }

    public void setUnitcost(String unitCost) {
        this.unitCost = unitCost;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}