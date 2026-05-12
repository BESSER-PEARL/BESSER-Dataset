





import java.util.List;
import java.util.ArrayList;

public class Elevator  {

    private boolean Direction;
    private int Current_Floor;
    private String attribute3;





    private Elevator_Controller elevator_controller;




    private Elevator_Controller elevator_controller;


    public Elevator(
        boolean Direction,        int Current_Floor,        String attribute3    ) {
        this.Direction = Direction;
        this.Current_Floor = Current_Floor;
        this.attribute3 = attribute3;
    }


    public boolean getDirection() {
        return Direction;
    }

    public void setDirection(boolean Direction) {
        this.Direction = Direction;
    }
    public int getCurrent_floor() {
        return Current_Floor;
    }

    public void setCurrent_floor(int Current_Floor) {
        this.Current_Floor = Current_Floor;
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