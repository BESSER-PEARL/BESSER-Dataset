





import java.util.List;
import java.util.ArrayList;

public class cartitem  {

    private float subtotal;
    private float unitcost;
    private int quantity;
    private int productId;





    private ShoppingCart shoppingcart;


    public cartitem(
        float subtotal,        float unitcost,        int quantity,        int productId    ) {
        this.subtotal = subtotal;
        this.unitcost = unitcost;
        this.quantity = quantity;
        this.productId = productId;
    }


    public float getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(float subtotal) {
        this.subtotal = subtotal;
    }
    public float getUnitcost() {
        return unitcost;
    }

    public void setUnitcost(float unitcost) {
        this.unitcost = unitcost;
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

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}