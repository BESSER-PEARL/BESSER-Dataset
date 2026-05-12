





import java.util.List;
import java.util.ArrayList;

public class Elevator  {

    private int currentFloor;
    private int number;
    private int destinationFloor;



    public Elevator(
        int currentFloor,        int number,        int destinationFloor    ) {
        this.currentFloor = currentFloor;
        this.number = number;
        this.destinationFloor = destinationFloor;
    }


    public int getCurrentfloor() {
        return currentFloor;
    }

    public void setCurrentfloor(int currentFloor) {
        this.currentFloor = currentFloor;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getDestinationfloor() {
        return destinationFloor;
    }

    public void setDestinationfloor(int destinationFloor) {
        this.destinationFloor = destinationFloor;
    }


}