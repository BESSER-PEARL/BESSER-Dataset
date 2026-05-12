





import java.util.List;
import java.util.ArrayList;

public class Controllers_OrderController  {






    private dao_LineItemDao_Interface dao_lineitemdao_interface;




    private dao_ShippingInfoDao_Interface dao_shippinginfodao_interface;




    private dao_OrderDao_Interface dao_orderdao_interface;


    public Controllers_OrderController(
    ) {
    }



    public dao_LineItemDao_Interface getDao_lineitemdao_interface() {
        return dao_lineitemdao_interface;
    }

    public void setDao_lineitemdao_interface(dao_LineItemDao_Interface dao_lineitemdao_interface) {
        this.dao_lineitemdao_interface = dao_lineitemdao_interface;
    }
    public dao_ShippingInfoDao_Interface getDao_shippinginfodao_interface() {
        return dao_shippinginfodao_interface;
    }

    public void setDao_shippinginfodao_interface(dao_ShippingInfoDao_Interface dao_shippinginfodao_interface) {
        this.dao_shippinginfodao_interface = dao_shippinginfodao_interface;
    }
    public dao_OrderDao_Interface getDao_orderdao_interface() {
        return dao_orderdao_interface;
    }

    public void setDao_orderdao_interface(dao_OrderDao_Interface dao_orderdao_interface) {
        this.dao_orderdao_interface = dao_orderdao_interface;
    }

}