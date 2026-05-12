





import java.util.List;
import java.util.ArrayList;

public class Models_ShippingInfo  {

    private String shippingtype;
    private int shippingcost;
    private int shippingid;
    private int shippingregionid;





    private Models_Order models_order;




    private dao_ShippingInfoDao_Interface dao_shippinginfodao_interface;


    public Models_ShippingInfo(
        String shippingtype,        int shippingcost,        int shippingid,        int shippingregionid    ) {
        this.shippingtype = shippingtype;
        this.shippingcost = shippingcost;
        this.shippingid = shippingid;
        this.shippingregionid = shippingregionid;
    }


    public String getShippingtype() {
        return shippingtype;
    }

    public void setShippingtype(String shippingtype) {
        this.shippingtype = shippingtype;
    }
    public int getShippingcost() {
        return shippingcost;
    }

    public void setShippingcost(int shippingcost) {
        this.shippingcost = shippingcost;
    }
    public int getShippingid() {
        return shippingid;
    }

    public void setShippingid(int shippingid) {
        this.shippingid = shippingid;
    }
    public int getShippingregionid() {
        return shippingregionid;
    }

    public void setShippingregionid(int shippingregionid) {
        this.shippingregionid = shippingregionid;
    }

    public Models_Order getModels_order() {
        return models_order;
    }

    public void setModels_order(Models_Order models_order) {
        this.models_order = models_order;
    }
    public dao_ShippingInfoDao_Interface getDao_shippinginfodao_interface() {
        return dao_shippinginfodao_interface;
    }

    public void setDao_shippinginfodao_interface(dao_ShippingInfoDao_Interface dao_shippinginfodao_interface) {
        this.dao_shippinginfodao_interface = dao_shippinginfodao_interface;
    }

}