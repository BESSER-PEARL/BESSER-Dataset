





import java.util.List;
import java.util.ArrayList;

public class orderDetail  {

    private float unitcost;
    private String productname;
    private int quantity;
    private float subtotall;
    private int productid;
    private int orderId;





    private product product;


    public orderDetail(
        float unitcost,        String productname,        int quantity,        float subtotall,        int productid,        int orderId    ) {
        this.unitcost = unitcost;
        this.productname = productname;
        this.quantity = quantity;
        this.subtotall = subtotall;
        this.productid = productid;
        this.orderId = orderId;
    }


    public float getUnitcost() {
        return unitcost;
    }

    public void setUnitcost(float unitcost) {
        this.unitcost = unitcost;
    }
    public String getProductname() {
        return productname;
    }

    public void setProductname(String productname) {
        this.productname = productname;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float getSubtotall() {
        return subtotall;
    }

    public void setSubtotall(float subtotall) {
        this.subtotall = subtotall;
    }
    public int getProductid() {
        return productid;
    }

    public void setProductid(int productid) {
        this.productid = productid;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }

    public product getProduct() {
        return product;
    }

    public void setProduct(product product) {
        this.product = product;
    }

}