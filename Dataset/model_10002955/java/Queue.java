





import java.util.List;
import java.util.ArrayList;

public class Queue  {

    private int floorQueue;
    private None currentDirection;





    private Elevator elevator;


    public Queue(
        int floorQueue,        None currentDirection    ) {
        this.floorQueue = floorQueue;
        this.currentDirection = currentDirection;
    }


    public int getFloorqueue() {
        return floorQueue;
    }

    public void setFloorqueue(int floorQueue) {
        this.floorQueue = floorQueue;
    }
    public None getCurrentdirection() {
        return currentDirection;
    }

    public void setCurrentdirection(None currentDirection) {
        this.currentDirection = currentDirection;
    }

    public Elevator getElevator() {
        return elevator;
    }

    public void setElevator(Elevator elevator) {
        this.elevator = elevator;
    }

}