





import java.util.List;
import java.util.ArrayList;

public class Level  {

    private int numofSpots;
    private int levelId;
    private String parkingSpots;





    private ParkingLot parkinglot;




    private List<ParkingSpot> parkingspots;


    public Level(
        int numofSpots,        int levelId,        String parkingSpots    ) {
        this.numofSpots = numofSpots;
        this.levelId = levelId;
        this.parkingSpots = parkingSpots;
        this.parkingspots = new ArrayList<>();
    }

    public Level(
        int numofSpots,        int levelId,        String parkingSpots        ArrayList<ParkingSpot> parkingspots    ) {
        this.numofSpots = numofSpots;
        this.levelId = levelId;
        this.parkingSpots = parkingSpots;
        this.parkingspots = parkingspots;
    }

    public int getNumofspots() {
        return numofSpots;
    }

    public void setNumofspots(int numofSpots) {
        this.numofSpots = numofSpots;
    }
    public int getLevelid() {
        return levelId;
    }

    public void setLevelid(int levelId) {
        this.levelId = levelId;
    }
    public String getParkingspots() {
        return parkingSpots;
    }

    public void setParkingspots(String parkingSpots) {
        this.parkingSpots = parkingSpots;
    }

    public ParkingLot getParkinglot() {
        return parkinglot;
    }

    public void setParkinglot(ParkingLot parkinglot) {
        this.parkinglot = parkinglot;
    }
    public List<ParkingSpot> getParkingspots() {
        return parkingspots;
    }

    public void addParkingspot(Parkingspot parkingspot) {
        this.parkingspots.add(parkingspot);
    }

}