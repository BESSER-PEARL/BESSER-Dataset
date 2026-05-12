





import java.util.List;
import java.util.ArrayList;

public class Order_Details  {

    private int productId;
    private None Payment__;
    private String productName;
    private None Report_Generation;
    private int unitCost;
    private int orderId;
    private int subTotal;
    private int quantity;



    public Order_Details(
        int productId,        None Payment__,        String productName,        None Report_Generation,        int unitCost,        int orderId,        int subTotal,        int quantity    ) {
        this.productId = productId;
        this.Payment__ = Payment__;
        this.productName = productName;
        this.Report_Generation = Report_Generation;
        this.unitCost = unitCost;
        this.orderId = orderId;
        this.subTotal = subTotal;
        this.quantity = quantity;
    }


    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public None getPayment__() {
        return Payment__;
    }

    public void setPayment__(None Payment__) {
        this.Payment__ = Payment__;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public None getReport_generation() {
        return Report_Generation;
    }

    public void setReport_generation(None Report_Generation) {
        this.Report_Generation = Report_Generation;
    }
    public int getUnitcost() {
        return unitCost;
    }

    public void setUnitcost(int unitCost) {
        this.unitCost = unitCost;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }
    public int getSubtotal() {
        return subTotal;
    }

    public void setSubtotal(int subTotal) {
        this.subTotal = subTotal;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}