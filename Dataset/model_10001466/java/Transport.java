





import java.util.List;
import java.util.ArrayList;

public class Transport  {

    private String transportCost;
    private int TransportID;
    private String location;





    private Orders orders;


    public Transport(
        String transportCost,        int TransportID,        String location    ) {
        this.transportCost = transportCost;
        this.TransportID = TransportID;
        this.location = location;
    }


    public String getTransportcost() {
        return transportCost;
    }

    public void setTransportcost(String transportCost) {
        this.transportCost = transportCost;
    }
    public int getTransportid() {
        return TransportID;
    }

    public void setTransportid(int TransportID) {
        this.TransportID = TransportID;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

}