





import java.util.List;
import java.util.ArrayList;

public class Controllers_ShoppingCartController  {






    private dao_CartItemDao_Interface dao_cartitemdao_interface;




    private dao_OrderDao_Interface dao_orderdao_interface;




    private dao_ShoppingCartDao_Interface dao_shoppingcartdao_interface;


    public Controllers_ShoppingCartController(
    ) {
    }



    public dao_CartItemDao_Interface getDao_cartitemdao_interface() {
        return dao_cartitemdao_interface;
    }

    public void setDao_cartitemdao_interface(dao_CartItemDao_Interface dao_cartitemdao_interface) {
        this.dao_cartitemdao_interface = dao_cartitemdao_interface;
    }
    public dao_OrderDao_Interface getDao_orderdao_interface() {
        return dao_orderdao_interface;
    }

    public void setDao_orderdao_interface(dao_OrderDao_Interface dao_orderdao_interface) {
        this.dao_orderdao_interface = dao_orderdao_interface;
    }
    public dao_ShoppingCartDao_Interface getDao_shoppingcartdao_interface() {
        return dao_shoppingcartdao_interface;
    }

    public void setDao_shoppingcartdao_interface(dao_ShoppingCartDao_Interface dao_shoppingcartdao_interface) {
        this.dao_shoppingcartdao_interface = dao_shoppingcartdao_interface;
    }

}