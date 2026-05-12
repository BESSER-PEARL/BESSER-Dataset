





import java.util.List;
import java.util.ArrayList;

public class Order_Details  {

    private int productId;
    private int quantity;
    private String productName;
    private int subtotal;
    private int unitcost;
    private int orderId;





    private Orders orders;


    public Order_Details(
        int productId,        int quantity,        String productName,        int subtotal,        int unitcost,        int orderId    ) {
        this.productId = productId;
        this.quantity = quantity;
        this.productName = productName;
        this.subtotal = subtotal;
        this.unitcost = unitcost;
        this.orderId = orderId;
    }


    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public int getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(int subtotal) {
        this.subtotal = subtotal;
    }
    public int getUnitcost() {
        return unitcost;
    }

    public void setUnitcost(int unitcost) {
        this.unitcost = unitcost;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

}