





import java.util.List;
import java.util.ArrayList;

public class hw2_Elevator  {

    private int numOfPassengers;
    private String passengersToFloor;
    private boolean isGoingUp;
    private int CAPACITY;
    private int currentFloorIndex;
    private int NUMBER_OF_FLOORS;





    private hw2_Building hw2_building;




    private hw2_Building hw2_building;


    public hw2_Elevator(
        int numOfPassengers,        String passengersToFloor,        boolean isGoingUp,        int CAPACITY,        int currentFloorIndex,        int NUMBER_OF_FLOORS    ) {
        this.numOfPassengers = numOfPassengers;
        this.passengersToFloor = passengersToFloor;
        this.isGoingUp = isGoingUp;
        this.CAPACITY = CAPACITY;
        this.currentFloorIndex = currentFloorIndex;
        this.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS;
    }


    public int getNumofpassengers() {
        return numOfPassengers;
    }

    public void setNumofpassengers(int numOfPassengers) {
        this.numOfPassengers = numOfPassengers;
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
    public int getCapacity() {
        return CAPACITY;
    }

    public void setCapacity(int CAPACITY) {
        this.CAPACITY = CAPACITY;
    }
    public int getCurrentfloorindex() {
        return currentFloorIndex;
    }

    public void setCurrentfloorindex(int currentFloorIndex) {
        this.currentFloorIndex = currentFloorIndex;
    }
    public int getNumber_of_floors() {
        return NUMBER_OF_FLOORS;
    }

    public void setNumber_of_floors(int NUMBER_OF_FLOORS) {
        this.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS;
    }

    public hw2_Building getHw2_building() {
        return hw2_building;
    }

    public void setHw2_building(hw2_Building hw2_building) {
        this.hw2_building = hw2_building;
    }
    public hw2_Building getHw2_building() {
        return hw2_building;
    }

    public void setHw2_building(hw2_Building hw2_building) {
        this.hw2_building = hw2_building;
    }

}