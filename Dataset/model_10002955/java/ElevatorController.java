





import java.util.List;
import java.util.ArrayList;

public class ElevatorController  {

    private None elevators;
    private None floors;



    public ElevatorController(
        None elevators,        None floors    ) {
        this.elevators = elevators;
        this.floors = floors;
    }


    public None getElevators() {
        return elevators;
    }

    public void setElevators(None elevators) {
        this.elevators = elevators;
    }
    public None getFloors() {
        return floors;
    }

    public void setFloors(None floors) {
        this.floors = floors;
    }


}