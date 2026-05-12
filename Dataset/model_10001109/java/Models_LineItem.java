





import java.util.List;
import java.util.ArrayList;

public class Models_LineItem  {

    private String productname;
    private int orderId;
    private float subtotal;
    private int quantity;
    private float unitcost;
    private int productid;





    private dao_LineItemDao_Interface dao_lineitemdao_interface;


    public Models_LineItem(
        String productname,        int orderId,        float subtotal,        int quantity,        float unitcost,        int productid    ) {
        this.productname = productname;
        this.orderId = orderId;
        this.subtotal = subtotal;
        this.quantity = quantity;
        this.unitcost = unitcost;
        this.productid = productid;
    }


    public String getProductname() {
        return productname;
    }

    public void setProductname(String productname) {
        this.productname = productname;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }
    public float getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(float subtotal) {
        this.subtotal = subtotal;
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
    public int getProductid() {
        return productid;
    }

    public void setProductid(int productid) {
        this.productid = productid;
    }

    public dao_LineItemDao_Interface getDao_lineitemdao_interface() {
        return dao_lineitemdao_interface;
    }

    public void setDao_lineitemdao_interface(dao_LineItemDao_Interface dao_lineitemdao_interface) {
        this.dao_lineitemdao_interface = dao_lineitemdao_interface;
    }

}