





import java.util.List;
import java.util.ArrayList;

public class Shipping_Info  {

    private int Shipping_Cost;
    private String Shipping_Type;
    private int Shipping_Id;
    private int ShippingRegionId;



    public Shipping_Info(
        int Shipping_Cost,        String Shipping_Type,        int Shipping_Id,        int ShippingRegionId    ) {
        this.Shipping_Cost = Shipping_Cost;
        this.Shipping_Type = Shipping_Type;
        this.Shipping_Id = Shipping_Id;
        this.ShippingRegionId = ShippingRegionId;
    }


    public int getShipping_cost() {
        return Shipping_Cost;
    }

    public void setShipping_cost(int Shipping_Cost) {
        this.Shipping_Cost = Shipping_Cost;
    }
    public String getShipping_type() {
        return Shipping_Type;
    }

    public void setShipping_type(String Shipping_Type) {
        this.Shipping_Type = Shipping_Type;
    }
    public int getShipping_id() {
        return Shipping_Id;
    }

    public void setShipping_id(int Shipping_Id) {
        this.Shipping_Id = Shipping_Id;
    }
    public int getShippingregionid() {
        return ShippingRegionId;
    }

    public void setShippingregionid(int ShippingRegionId) {
        this.ShippingRegionId = ShippingRegionId;
    }


}