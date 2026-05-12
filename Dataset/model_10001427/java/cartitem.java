





import java.util.List;
import java.util.ArrayList;

public class cartitem  {

    private int product;
    private String name;
    private int quantity;
    private float unitcost;
    private float subtotal;





    private ShoppingCart shoppingcart;


    public cartitem(
        int product,        String name,        int quantity,        float unitcost,        float subtotal    ) {
        this.product = product;
        this.name = name;
        this.quantity = quantity;
        this.unitcost = unitcost;
        this.subtotal = subtotal;
    }


    public int getProduct() {
        return product;
    }

    public void setProduct(int product) {
        this.product = product;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public float getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(float subtotal) {
        this.subtotal = subtotal;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}