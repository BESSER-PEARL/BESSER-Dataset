





import java.util.List;
import java.util.ArrayList;

public class orderDetail  {

    private int productid;
    private int orderId;
    private String productname;
    private int quantity;
    private float unitcost;
    private float subtotall;





    private product product;


    public orderDetail(
        int productid,        int orderId,        String productname,        int quantity,        float unitcost,        float subtotall    ) {
        this.productid = productid;
        this.orderId = orderId;
        this.productname = productname;
        this.quantity = quantity;
        this.unitcost = unitcost;
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
    public float getUnitcost() {
        return unitcost;
    }

    public void setUnitcost(float unitcost) {
        this.unitcost = unitcost;
    }
    public float getSubtotall() {
        return subtotall;
    }

    public void setSubtotall(float subtotall) {
        this.subtotall = subtotall;
    }

    public product getProduct() {
        return product;
    }

    public void setProduct(product product) {
        this.product = product;
    }

}