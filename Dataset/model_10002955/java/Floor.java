





import java.util.List;
import java.util.ArrayList;

public class Floor  {

    private int floorID;
    private None floorButtons;





    private ElevatorController elevatorcontroller;


    public Floor(
        int floorID,        None floorButtons    ) {
        this.floorID = floorID;
        this.floorButtons = floorButtons;
    }


    public int getFloorid() {
        return floorID;
    }

    public void setFloorid(int floorID) {
        this.floorID = floorID;
    }
    public None getFloorbuttons() {
        return floorButtons;
    }

    public void setFloorbuttons(None floorButtons) {
        this.floorButtons = floorButtons;
    }

    public ElevatorController getElevatorcontroller() {
        return elevatorcontroller;
    }

    public void setElevatorcontroller(ElevatorController elevatorcontroller) {
        this.elevatorcontroller = elevatorcontroller;
    }

}