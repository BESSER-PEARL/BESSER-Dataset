





import java.util.List;
import java.util.ArrayList;

public class orderDetail  {

    private float subtotall;
    private int quantity;
    private int productid;
    private int orderId;
    private float unitcost;
    private String productname;



    public orderDetail(
        float subtotall,        int quantity,        int productid,        int orderId,        float unitcost,        String productname    ) {
        this.subtotall = subtotall;
        this.quantity = quantity;
        this.productid = productid;
        this.orderId = orderId;
        this.unitcost = unitcost;
        this.productname = productname;
    }


    public float getSubtotall() {
        return subtotall;
    }

    public void setSubtotall(float subtotall) {
        this.subtotall = subtotall;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
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


}