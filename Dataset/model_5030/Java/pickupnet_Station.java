





import java.util.List;
import java.util.ArrayList;

public class pickupnet_Station  {






    private List<pickupnet_Shipment> pickupnet_shipments;




    private List<pickupnet_Customer> pickupnet_customers;




    private List<pickupnet_Driver> pickupnet_drivers;


    public pickupnet_Station(
    ) {
        this.pickupnet_shipments = new ArrayList<>();
        this.pickupnet_customers = new ArrayList<>();
        this.pickupnet_drivers = new ArrayList<>();
    }

    public pickupnet_Station(
        ArrayList<pickupnet_Shipment> pickupnet_shipments,        ArrayList<pickupnet_Customer> pickupnet_customers,        ArrayList<pickupnet_Driver> pickupnet_drivers    ) {
        this.pickupnet_shipments = pickupnet_shipments;
        this.pickupnet_customers = pickupnet_customers;
        this.pickupnet_drivers = pickupnet_drivers;
    }


    public List<pickupnet_Shipment> getPickupnet_shipments() {
        return pickupnet_shipments;
    }

    public void addPickupnet_shipment(Pickupnet_shipment pickupnet_shipment) {
        this.pickupnet_shipments.add(pickupnet_shipment);
    }
    public List<pickupnet_Customer> getPickupnet_customers() {
        return pickupnet_customers;
    }

    public void addPickupnet_customer(Pickupnet_customer pickupnet_customer) {
        this.pickupnet_customers.add(pickupnet_customer);
    }
    public List<pickupnet_Driver> getPickupnet_drivers() {
        return pickupnet_drivers;
    }

    public void addPickupnet_driver(Pickupnet_driver pickupnet_driver) {
        this.pickupnet_drivers.add(pickupnet_driver);
    }

}