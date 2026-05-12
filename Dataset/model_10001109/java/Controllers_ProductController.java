





import java.util.List;
import java.util.ArrayList;

public class Controllers_ProductController  {






    private dao_ProductDao_Interface dao_productdao_interface;




    private dao_ShoppingCartDao_Interface dao_shoppingcartdao_interface;


    public Controllers_ProductController(
    ) {
    }



    public dao_ProductDao_Interface getDao_productdao_interface() {
        return dao_productdao_interface;
    }

    public void setDao_productdao_interface(dao_ProductDao_Interface dao_productdao_interface) {
        this.dao_productdao_interface = dao_productdao_interface;
    }
    public dao_ShoppingCartDao_Interface getDao_shoppingcartdao_interface() {
        return dao_shoppingcartdao_interface;
    }

    public void setDao_shoppingcartdao_interface(dao_ShoppingCartDao_Interface dao_shoppingcartdao_interface) {
        this.dao_shoppingcartdao_interface = dao_shoppingcartdao_interface;
    }

}