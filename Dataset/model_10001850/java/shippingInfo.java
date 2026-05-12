





import java.util.List;
import java.util.ArrayList;

public class shippingInfo  {

    private int shippingCost;
    private None View_Shipping_Status__;
    private String shippingType;
    private int shippingId;
    private int shippingRegionId;



    public shippingInfo(
        int shippingCost,        None View_Shipping_Status__,        String shippingType,        int shippingId,        int shippingRegionId    ) {
        this.shippingCost = shippingCost;
        this.View_Shipping_Status__ = View_Shipping_Status__;
        this.shippingType = shippingType;
        this.shippingId = shippingId;
        this.shippingRegionId = shippingRegionId;
    }


    public int getShippingcost() {
        return shippingCost;
    }

    public void setShippingcost(int shippingCost) {
        this.shippingCost = shippingCost;
    }
    public None getView_shipping_status__() {
        return View_Shipping_Status__;
    }

    public void setView_shipping_status__(None View_Shipping_Status__) {
        this.View_Shipping_Status__ = View_Shipping_Status__;
    }
    public String getShippingtype() {
        return shippingType;
    }

    public void setShippingtype(String shippingType) {
        this.shippingType = shippingType;
    }
    public int getShippingid() {
        return shippingId;
    }

    public void setShippingid(int shippingId) {
        this.shippingId = shippingId;
    }
    public int getShippingregionid() {
        return shippingRegionId;
    }

    public void setShippingregionid(int shippingRegionId) {
        this.shippingRegionId = shippingRegionId;
    }


}