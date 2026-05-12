





import java.util.List;
import java.util.ArrayList;

public class cartitem  {

    private int productId;
    private float subtotal;
    private int quantity;
    private float unitcost;





    private ShoppingCart shoppingcart;


    public cartitem(
        int productId,        float subtotal,        int quantity,        float unitcost    ) {
        this.productId = productId;
        this.subtotal = subtotal;
        this.quantity = quantity;
        this.unitcost = unitcost;
    }


    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
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

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}