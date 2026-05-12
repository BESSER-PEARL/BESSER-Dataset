





import java.util.List;
import java.util.ArrayList;

public class ShippingInfo  {

    private int ShippingRegionID;
    private String ShippingType;
    private int ShippingID;
    private int ShippingCost;





    private Order order;


    public ShippingInfo(
        int ShippingRegionID,        String ShippingType,        int ShippingID,        int ShippingCost    ) {
        this.ShippingRegionID = ShippingRegionID;
        this.ShippingType = ShippingType;
        this.ShippingID = ShippingID;
        this.ShippingCost = ShippingCost;
    }


    public int getShippingregionid() {
        return ShippingRegionID;
    }

    public void setShippingregionid(int ShippingRegionID) {
        this.ShippingRegionID = ShippingRegionID;
    }
    public String getShippingtype() {
        return ShippingType;
    }

    public void setShippingtype(String ShippingType) {
        this.ShippingType = ShippingType;
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

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}