





import java.util.List;
import java.util.ArrayList;

public class ParkingLot  {

    private int numOfLevels;
    private String hours;
    private int spotsOccupied;
    private int capacity;
    private String levels;



    public ParkingLot(
        int numOfLevels,        String hours,        int spotsOccupied,        int capacity,        String levels    ) {
        this.numOfLevels = numOfLevels;
        this.hours = hours;
        this.spotsOccupied = spotsOccupied;
        this.capacity = capacity;
        this.levels = levels;
    }


    public int getNumoflevels() {
        return numOfLevels;
    }

    public void setNumoflevels(int numOfLevels) {
        this.numOfLevels = numOfLevels;
    }
    public String getHours() {
        return hours;
    }

    public void setHours(String hours) {
        this.hours = hours;
    }
    public int getSpotsoccupied() {
        return spotsOccupied;
    }

    public void setSpotsoccupied(int spotsOccupied) {
        this.spotsOccupied = spotsOccupied;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getLevels() {
        return levels;
    }

    public void setLevels(String levels) {
        this.levels = levels;
    }


}