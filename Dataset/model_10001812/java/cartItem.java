





import java.util.List;
import java.util.ArrayList;

public class cartItem  {

    private int productId;
    private String unitCost;
    private String name;
    private String subtotal;
    private int quantity;





    private Product product;




    private cartItem cartitem;


    public cartItem(
        int productId,        String unitCost,        String name,        String subtotal,        int quantity    ) {
        this.productId = productId;
        this.unitCost = unitCost;
        this.name = name;
        this.subtotal = subtotal;
        this.quantity = quantity;
    }


    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public String getUnitcost() {
        return unitCost;
    }

    public void setUnitcost(String unitCost) {
        this.unitCost = unitCost;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(String subtotal) {
        this.subtotal = subtotal;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }
    public cartItem getCartitem() {
        return cartitem;
    }

    public void setCartitem(cartItem cartitem) {
        this.cartitem = cartitem;
    }

}