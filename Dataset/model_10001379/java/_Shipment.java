





import java.util.List;
import java.util.ArrayList;

public class _Shipment  {

    private int orderId;
    private int shipmentNumber;





    private Farmer farmer;


    public _Shipment(
        int orderId,        int shipmentNumber    ) {
        this.orderId = orderId;
        this.shipmentNumber = shipmentNumber;
    }


    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }
    public int getShipmentnumber() {
        return shipmentNumber;
    }

    public void setShipmentnumber(int shipmentNumber) {
        this.shipmentNumber = shipmentNumber;
    }

    public Farmer getFarmer() {
        return farmer;
    }

    public void setFarmer(Farmer farmer) {
        this.farmer = farmer;
    }

}