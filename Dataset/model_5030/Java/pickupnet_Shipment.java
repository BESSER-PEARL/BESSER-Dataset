





import java.util.List;
import java.util.ArrayList;

public class pickupnet_Shipment  {

    private String id;
    private String status;





    private pickupnet_Customer pickupnet_customer;




    private pickupnet_Driver pickupnet_driver;




    private pickupnet_Customer pickupnet_customer;




    private pickupnet_Driver pickupnet_driver;


    public pickupnet_Shipment(
        String id,        String status    ) {
        this.id = id;
        this.status = status;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public pickupnet_Customer getPickupnet_customer() {
        return pickupnet_customer;
    }

    public void setPickupnet_customer(pickupnet_Customer pickupnet_customer) {
        this.pickupnet_customer = pickupnet_customer;
    }
    public pickupnet_Driver getPickupnet_driver() {
        return pickupnet_driver;
    }

    public void setPickupnet_driver(pickupnet_Driver pickupnet_driver) {
        this.pickupnet_driver = pickupnet_driver;
    }
    public pickupnet_Customer getPickupnet_customer() {
        return pickupnet_customer;
    }

    public void setPickupnet_customer(pickupnet_Customer pickupnet_customer) {
        this.pickupnet_customer = pickupnet_customer;
    }
    public pickupnet_Driver getPickupnet_driver() {
        return pickupnet_driver;
    }

    public void setPickupnet_driver(pickupnet_Driver pickupnet_driver) {
        this.pickupnet_driver = pickupnet_driver;
    }

}