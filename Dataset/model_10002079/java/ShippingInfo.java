





import java.util.List;
import java.util.ArrayList;

public class ShippingInfo  {

    private int ShippingRegionID;
    private int ShippingID;
    private int ShippingCost;
    private String ShippingType;





    private Order order;


    public ShippingInfo(
        int ShippingRegionID,        int ShippingID,        int ShippingCost,        String ShippingType    ) {
        this.ShippingRegionID = ShippingRegionID;
        this.ShippingID = ShippingID;
        this.ShippingCost = ShippingCost;
        this.ShippingType = ShippingType;
    }


    public int getShippingregionid() {
        return ShippingRegionID;
    }

    public void setShippingregionid(int ShippingRegionID) {
        this.ShippingRegionID = ShippingRegionID;
    }
    public int getShippingid() {
        return ShippingID;
    }

    public void setShippingid(int ShippingID) {
        this.ShippingID = ShippingID;
    }
    public int getShippingcost() {
        return ShippingCost;
    }

    public void setShippingcost(int ShippingCost) {
        this.ShippingCost = ShippingCost;
    }
    public String getShippingtype() {
        return ShippingType;
    }

    public void setShippingtype(String ShippingType) {
        this.ShippingType = ShippingType;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}