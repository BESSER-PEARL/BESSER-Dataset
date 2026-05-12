





import java.util.List;
import java.util.ArrayList;

public class elevator_Elevator  {

    private int NUMBER_OF_FLOORS;
    private String passengersToFloor;
    private boolean isGoingUp;
    private int currentFloor;
    private int numOfPassengers;



    public elevator_Elevator(
        int NUMBER_OF_FLOORS,        String passengersToFloor,        boolean isGoingUp,        int currentFloor,        int numOfPassengers    ) {
        this.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS;
        this.passengersToFloor = passengersToFloor;
        this.isGoingUp = isGoingUp;
        this.currentFloor = currentFloor;
        this.numOfPassengers = numOfPassengers;
    }


    public int getNumber_of_floors() {
        return NUMBER_OF_FLOORS;
    }

    public void setNumber_of_floors(int NUMBER_OF_FLOORS) {
        this.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS;
    }
    public String getPassengerstofloor() {
        return passengersToFloor;
    }

    public void setPassengerstofloor(String passengersToFloor) {
        this.passengersToFloor = passengersToFloor;
    }
    public boolean getIsgoingup() {
        return isGoingUp;
    }

    public void setIsgoingup(boolean isGoingUp) {
        this.isGoingUp = isGoingUp;
    }
    public int getCurrentfloor() {
        return currentFloor;
    }

    public void setCurrentfloor(int currentFloor) {
        this.currentFloor = currentFloor;
    }
    public int getNumofpassengers() {
        return numOfPassengers;
    }

    public void setNumofpassengers(int numOfPassengers) {
        this.numOfPassengers = numOfPassengers;
    }


}