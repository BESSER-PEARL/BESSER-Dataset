





import java.util.List;
import java.util.ArrayList;

public class Sensor  {

    private boolean Status;
    private int SensorID;
    private int SensorType;





    private System system;


    public Sensor(
        boolean Status,        int SensorID,        int SensorType    ) {
        this.Status = Status;
        this.SensorID = SensorID;
        this.SensorType = SensorType;
    }


    public boolean getStatus() {
        return Status;
    }

    public void setStatus(boolean Status) {
        this.Status = Status;
    }
    public int getSensorid() {
        return SensorID;
    }

    public void setSensorid(int SensorID) {
        this.SensorID = SensorID;
    }
    public int getSensortype() {
        return SensorType;
    }

    public void setSensortype(int SensorType) {
        this.SensorType = SensorType;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}