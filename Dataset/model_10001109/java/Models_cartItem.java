





import java.util.List;
import java.util.ArrayList;

public class Models_cartItem  {

    private int quantity;
    private int cartId;
    private String name;
    private float unitcost;
    private float subtotal;
    private boolean deleted;





    private Models_ShoppingCart models_shoppingcart;




    private dao_CartItemDao_Interface dao_cartitemdao_interface;




    private Models_Product models_product;


    public Models_cartItem(
        int quantity,        int cartId,        String name,        float unitcost,        float subtotal,        boolean deleted    ) {
        this.quantity = quantity;
        this.cartId = cartId;
        this.name = name;
        this.unitcost = unitcost;
        this.subtotal = subtotal;
        this.deleted = deleted;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getCartid() {
        return cartId;
    }

    public void setCartid(int cartId) {
        this.cartId = cartId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public boolean getDeleted() {
        return deleted;
    }

    public void setDeleted(boolean deleted) {
        this.deleted = deleted;
    }

    public Models_ShoppingCart getModels_shoppingcart() {
        return models_shoppingcart;
    }

    public void setModels_shoppingcart(Models_ShoppingCart models_shoppingcart) {
        this.models_shoppingcart = models_shoppingcart;
    }
    public dao_CartItemDao_Interface getDao_cartitemdao_interface() {
        return dao_cartitemdao_interface;
    }

    public void setDao_cartitemdao_interface(dao_CartItemDao_Interface dao_cartitemdao_interface) {
        this.dao_cartitemdao_interface = dao_cartitemdao_interface;
    }
    public Models_Product getModels_product() {
        return models_product;
    }

    public void setModels_product(Models_Product models_product) {
        this.models_product = models_product;
    }

}