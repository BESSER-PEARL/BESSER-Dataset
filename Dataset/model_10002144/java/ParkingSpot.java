





import java.util.List;
import java.util.ArrayList;

public class ParkingSpot  {

    private None spotType;
    private boolean occupied;
    private int parkingSpotId;



    public ParkingSpot(
        None spotType,        boolean occupied,        int parkingSpotId    ) {
        this.spotType = spotType;
        this.occupied = occupied;
        this.parkingSpotId = parkingSpotId;
    }


    public None getSpottype() {
        return spotType;
    }

    public void setSpottype(None spotType) {
        this.spotType = spotType;
    }
    public boolean getOccupied() {
        return occupied;
    }

    public void setOccupied(boolean occupied) {
        this.occupied = occupied;
    }
    public int getParkingspotid() {
        return parkingSpotId;
    }

    public void setParkingspotid(int parkingSpotId) {
        this.parkingSpotId = parkingSpotId;
    }


}