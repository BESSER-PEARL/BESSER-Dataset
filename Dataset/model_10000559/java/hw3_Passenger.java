





import java.util.List;
import java.util.ArrayList;

public class hw3_Passenger  {

    private int currentFloor;
    private int id;
    private int destinationFloor;
    private int UNDEFINED_FLOOR;





    private hw3_Floor hw3_floor;




    private hw3_Floor hw3_floor;




    private hw3_Floor hw3_floor;




    private hw3_Elevator hw3_elevator;


    public hw3_Passenger(
        int currentFloor,        int id,        int destinationFloor,        int UNDEFINED_FLOOR    ) {
        this.currentFloor = currentFloor;
        this.id = id;
        this.destinationFloor = destinationFloor;
        this.UNDEFINED_FLOOR = UNDEFINED_FLOOR;
    }


    public int getCurrentfloor() {
        return currentFloor;
    }

    public void setCurrentfloor(int currentFloor) {
        this.currentFloor = currentFloor;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getDestinationfloor() {
        return destinationFloor;
    }

    public void setDestinationfloor(int destinationFloor) {
        this.destinationFloor = destinationFloor;
    }
    public int getUndefined_floor() {
        return UNDEFINED_FLOOR;
    }

    public void setUndefined_floor(int UNDEFINED_FLOOR) {
        this.UNDEFINED_FLOOR = UNDEFINED_FLOOR;
    }

    public hw3_Floor getHw3_floor() {
        return hw3_floor;
    }

    public void setHw3_floor(hw3_Floor hw3_floor) {
        this.hw3_floor = hw3_floor;
    }
    public hw3_Floor getHw3_floor() {
        return hw3_floor;
    }

    public void setHw3_floor(hw3_Floor hw3_floor) {
        this.hw3_floor = hw3_floor;
    }
    public hw3_Floor getHw3_floor() {
        return hw3_floor;
    }

    public void setHw3_floor(hw3_Floor hw3_floor) {
        this.hw3_floor = hw3_floor;
    }
    public hw3_Elevator getHw3_elevator() {
        return hw3_elevator;
    }

    public void setHw3_elevator(hw3_Elevator hw3_elevator) {
        this.hw3_elevator = hw3_elevator;
    }

}