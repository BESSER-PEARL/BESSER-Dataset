





import java.util.List;
import java.util.ArrayList;

public class OrderDetail  {

    private int productId;
    private int quantity;
    private float subtotal;
    private float unitCost;
    private int ordrId;
    private String productName;





    private Order order;


    public OrderDetail(
        int productId,        int quantity,        float subtotal,        float unitCost,        int ordrId,        String productName    ) {
        this.productId = productId;
        this.quantity = quantity;
        this.subtotal = subtotal;
        this.unitCost = unitCost;
        this.ordrId = ordrId;
        this.productName = productName;
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
    public float getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(float subtotal) {
        this.subtotal = subtotal;
    }
    public float getUnitcost() {
        return unitCost;
    }

    public void setUnitcost(float unitCost) {
        this.unitCost = unitCost;
    }
    public int getOrdrid() {
        return ordrId;
    }

    public void setOrdrid(int ordrId) {
        this.ordrId = ordrId;
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