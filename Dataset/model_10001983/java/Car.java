





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private None destination;
    private String direction;
    private None stopLoader;
    private int weightLoad;
    private String destQueue;
    private String stopQueue;
    private None box;
    private int location;
    private int WEIGHT_LIMIT;
    private int floorNum;



    public Car(
        None destination,        String direction,        None stopLoader,        int weightLoad,        String destQueue,        String stopQueue,        None box,        int location,        int WEIGHT_LIMIT,        int floorNum    ) {
        this.destination = destination;
        this.direction = direction;
        this.stopLoader = stopLoader;
        this.weightLoad = weightLoad;
        this.destQueue = destQueue;
        this.stopQueue = stopQueue;
        this.box = box;
        this.location = location;
        this.WEIGHT_LIMIT = WEIGHT_LIMIT;
        this.floorNum = floorNum;
    }


    public None getDestination() {
        return destination;
    }

    public void setDestination(None destination) {
        this.destination = destination;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public None getStoploader() {
        return stopLoader;
    }

    public void setStoploader(None stopLoader) {
        this.stopLoader = stopLoader;
    }
    public int getWeightload() {
        return weightLoad;
    }

    public void setWeightload(int weightLoad) {
        this.weightLoad = weightLoad;
    }
    public String getDestqueue() {
        return destQueue;
    }

    public void setDestqueue(String destQueue) {
        this.destQueue = destQueue;
    }
    public String getStopqueue() {
        return stopQueue;
    }

    public void setStopqueue(String stopQueue) {
        this.stopQueue = stopQueue;
    }
    public None getBox() {
        return box;
    }

    public void setBox(None box) {
        this.box = box;
    }
    public int getLocation() {
        return location;
    }

    public void setLocation(int location) {
        this.location = location;
    }
    public int getWeight_limit() {
        return WEIGHT_LIMIT;
    }

    public void setWeight_limit(int WEIGHT_LIMIT) {
        this.WEIGHT_LIMIT = WEIGHT_LIMIT;
    }
    public int getFloornum() {
        return floorNum;
    }

    public void setFloornum(int floorNum) {
        this.floorNum = floorNum;
    }


}