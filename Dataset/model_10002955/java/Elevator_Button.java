





import java.util.List;
import java.util.ArrayList;

public class Elevator_Button  {

    private int floorID;





    private Elevator elevator;


    public Elevator_Button(
        int floorID    ) {
        this.floorID = floorID;
    }


    public int getFloorid() {
        return floorID;
    }

    public void setFloorid(int floorID) {
        this.floorID = floorID;
    }

    public Elevator getElevator() {
        return elevator;
    }

    public void setElevator(Elevator elevator) {
        this.elevator = elevator;
    }

}