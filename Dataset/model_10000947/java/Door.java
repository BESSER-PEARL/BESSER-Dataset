





import java.util.List;
import java.util.ArrayList;

public class Door  {

    private int DoorID;





    private Sensor sensor;


    public Door(
        int DoorID    ) {
        this.DoorID = DoorID;
    }


    public int getDoorid() {
        return DoorID;
    }

    public void setDoorid(int DoorID) {
        this.DoorID = DoorID;
    }

    public Sensor getSensor() {
        return sensor;
    }

    public void setSensor(Sensor sensor) {
        this.sensor = sensor;
    }

}