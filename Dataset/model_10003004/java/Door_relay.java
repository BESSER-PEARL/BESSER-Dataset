





import java.util.List;
import java.util.ArrayList;

public class Door_relay  {

    private int DoorID;
    private String DoorOpen;



    public Door_relay(
        int DoorID,        String DoorOpen    ) {
        this.DoorID = DoorID;
        this.DoorOpen = DoorOpen;
    }


    public int getDoorid() {
        return DoorID;
    }

    public void setDoorid(int DoorID) {
        this.DoorID = DoorID;
    }
    public String getDooropen() {
        return DoorOpen;
    }

    public void setDooropen(String DoorOpen) {
        this.DoorOpen = DoorOpen;
    }


}