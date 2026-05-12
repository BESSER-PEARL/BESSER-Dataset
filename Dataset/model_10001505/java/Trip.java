





import java.util.List;
import java.util.ArrayList;

public class Trip  {

    private boolean isIntercity;
    private int freeSeats;
    private int capacity;
    private String time;
    private None route;
    private None driver;
    private String uid;
    private String seatPrice;
    private boolean isLive;
    private int reservedSeats;



    public Trip(
        boolean isIntercity,        int freeSeats,        int capacity,        String time,        None route,        None driver,        String uid,        String seatPrice,        boolean isLive,        int reservedSeats    ) {
        this.isIntercity = isIntercity;
        this.freeSeats = freeSeats;
        this.capacity = capacity;
        this.time = time;
        this.route = route;
        this.driver = driver;
        this.uid = uid;
        this.seatPrice = seatPrice;
        this.isLive = isLive;
        this.reservedSeats = reservedSeats;
    }


    public boolean getIsintercity() {
        return isIntercity;
    }

    public void setIsintercity(boolean isIntercity) {
        this.isIntercity = isIntercity;
    }
    public int getFreeseats() {
        return freeSeats;
    }

    public void setFreeseats(int freeSeats) {
        this.freeSeats = freeSeats;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public None getRoute() {
        return route;
    }

    public void setRoute(None route) {
        this.route = route;
    }
    public None getDriver() {
        return driver;
    }

    public void setDriver(None driver) {
        this.driver = driver;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getSeatprice() {
        return seatPrice;
    }

    public void setSeatprice(String seatPrice) {
        this.seatPrice = seatPrice;
    }
    public boolean getIslive() {
        return isLive;
    }

    public void setIslive(boolean isLive) {
        this.isLive = isLive;
    }
    public int getReservedseats() {
        return reservedSeats;
    }

    public void setReservedseats(int reservedSeats) {
        this.reservedSeats = reservedSeats;
    }


}