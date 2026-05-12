





import java.util.List;
import java.util.ArrayList;

public class hw3_Elevator  {

    private int NUMBER_OF_FLOORS;
    private int numOfPassengers;
    private int currentFloorIndex;
    private boolean isGoingUp;
    private int CAPACITY;
    private String passengersToFloor;





    private hw3_Building hw3_building;




    private hw3_Building hw3_building;


    public hw3_Elevator(
        int NUMBER_OF_FLOORS,        int numOfPassengers,        int currentFloorIndex,        boolean isGoingUp,        int CAPACITY,        String passengersToFloor    ) {
        this.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS;
        this.numOfPassengers = numOfPassengers;
        this.currentFloorIndex = currentFloorIndex;
        this.isGoingUp = isGoingUp;
        this.CAPACITY = CAPACITY;
        this.passengersToFloor = passengersToFloor;
    }


    public int getNumber_of_floors() {
        return NUMBER_OF_FLOORS;
    }

    public void setNumber_of_floors(int NUMBER_OF_FLOORS) {
        this.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS;
    }
    public int getNumofpassengers() {
        return numOfPassengers;
    }

    public void setNumofpassengers(int numOfPassengers) {
        this.numOfPassengers = numOfPassengers;
    }
    public int getCurrentfloorindex() {
        return currentFloorIndex;
    }

    public void setCurrentfloorindex(int currentFloorIndex) {
        this.currentFloorIndex = currentFloorIndex;
    }
    public boolean getIsgoingup() {
        return isGoingUp;
    }

    public void setIsgoingup(boolean isGoingUp) {
        this.isGoingUp = isGoingUp;
    }
    public int getCapacity() {
        return CAPACITY;
    }

    public void setCapacity(int CAPACITY) {
        this.CAPACITY = CAPACITY;
    }
    public String getPassengerstofloor() {
        return passengersToFloor;
    }

    public void setPassengerstofloor(String passengersToFloor) {
        this.passengersToFloor = passengersToFloor;
    }

    public hw3_Building getHw3_building() {
        return hw3_building;
    }

    public void setHw3_building(hw3_Building hw3_building) {
        this.hw3_building = hw3_building;
    }
    public hw3_Building getHw3_building() {
        return hw3_building;
    }

    public void setHw3_building(hw3_Building hw3_building) {
        this.hw3_building = hw3_building;
    }

}