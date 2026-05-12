





import java.util.List;
import java.util.ArrayList;

public class Sensor  {

    private int SensorType;
    private int SensorID;





    private Door door;




    private System___mirror system___mirror;


    public Sensor(
        int SensorType,        int SensorID    ) {
        this.SensorType = SensorType;
        this.SensorID = SensorID;
    }


    public int getSensortype() {
        return SensorType;
    }

    public void setSensortype(int SensorType) {
        this.SensorType = SensorType;
    }
    public int getSensorid() {
        return SensorID;
    }

    public void setSensorid(int SensorID) {
        this.SensorID = SensorID;
    }

    public Door getDoor() {
        return door;
    }

    public void setDoor(Door door) {
        this.door = door;
    }
    public System___mirror getSystem___mirror() {
        return system___mirror;
    }

    public void setSystem___mirror(System___mirror system___mirror) {
        this.system___mirror = system___mirror;
    }

}