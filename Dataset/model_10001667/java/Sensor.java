





import java.util.List;
import java.util.ArrayList;

public class Sensor  {

    private int SensorType;
    private int SensorID;





    private Hub_Device hub_device;


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

    public Hub_Device getHub_device() {
        return hub_device;
    }

    public void setHub_device(Hub_Device hub_device) {
        this.hub_device = hub_device;
    }

}