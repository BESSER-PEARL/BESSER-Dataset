





import java.util.List;
import java.util.ArrayList;

public class Elevator  {

    private int Current_Floor;
    private boolean Direction;
    private String attribute3;





    private Elevator_Controller elevator_controller;




    private Elevator_Controller elevator_controller;


    public Elevator(
        int Current_Floor,        boolean Direction,        String attribute3    ) {
        this.Current_Floor = Current_Floor;
        this.Direction = Direction;
        this.attribute3 = attribute3;
    }


    public int getCurrent_floor() {
        return Current_Floor;
    }

    public void setCurrent_floor(int Current_Floor) {
        this.Current_Floor = Current_Floor;
    }
    public boolean getDirection() {
        return Direction;
    }

    public void setDirection(boolean Direction) {
        this.Direction = Direction;
    }
    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }

    public Elevator_Controller getElevator_controller() {
        return elevator_controller;
    }

    public void setElevator_controller(Elevator_Controller elevator_controller) {
        this.elevator_controller = elevator_controller;
    }
    public Elevator_Controller getElevator_controller() {
        return elevator_controller;
    }

    public void setElevator_controller(Elevator_Controller elevator_controller) {
        this.elevator_controller = elevator_controller;
    }

}