





import java.util.List;
import java.util.ArrayList;

public class Sensor  {

    private int SensorType;
    private int SensorID;





    private System system;


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

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}