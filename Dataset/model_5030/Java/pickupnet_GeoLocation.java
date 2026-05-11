





import java.util.List;
import java.util.ArrayList;

public class pickupnet_GeoLocation  {

    private float lat;
    private float lon;





    private pickupnet_Address pickupnet_address;


    public pickupnet_GeoLocation(
        float lat,        float lon    ) {
        this.lat = lat;
        this.lon = lon;
    }


    public float getLat() {
        return lat;
    }

    public void setLat(float lat) {
        this.lat = lat;
    }
    public float getLon() {
        return lon;
    }

    public void setLon(float lon) {
        this.lon = lon;
    }

    public pickupnet_Address getPickupnet_address() {
        return pickupnet_address;
    }

    public void setPickupnet_address(pickupnet_Address pickupnet_address) {
        this.pickupnet_address = pickupnet_address;
    }

}