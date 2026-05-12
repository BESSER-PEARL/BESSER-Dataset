





import java.util.List;
import java.util.ArrayList;

public class Models_ShoppingCart  {

    private int status;
    private int customerId;
    private int dateAdded;
    private boolean deleted;
    private int cartId;





    private dao_ShoppingCartDao_Interface dao_shoppingcartdao_interface;


    public Models_ShoppingCart(
        int status,        int customerId,        int dateAdded,        boolean deleted,        int cartId    ) {
        this.status = status;
        this.customerId = customerId;
        this.dateAdded = dateAdded;
        this.deleted = deleted;
        this.cartId = cartId;
    }


    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public int getCustomerid() {
        return customerId;
    }

    public void setCustomerid(int customerId) {
        this.customerId = customerId;
    }
    public int getDateadded() {
        return dateAdded;
    }

    public void setDateadded(int dateAdded) {
        this.dateAdded = dateAdded;
    }
    public boolean getDeleted() {
        return deleted;
    }

    public void setDeleted(boolean deleted) {
        this.deleted = deleted;
    }
    public int getCartid() {
        return cartId;
    }

    public void setCartid(int cartId) {
        this.cartId = cartId;
    }

    public dao_ShoppingCartDao_Interface getDao_shoppingcartdao_interface() {
        return dao_shoppingcartdao_interface;
    }

    public void setDao_shoppingcartdao_interface(dao_ShoppingCartDao_Interface dao_shoppingcartdao_interface) {
        this.dao_shoppingcartdao_interface = dao_shoppingcartdao_interface;
    }

}