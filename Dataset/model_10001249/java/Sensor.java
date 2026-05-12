





import java.util.List;
import java.util.ArrayList;

public class Sensor  {

    private int SensorID;
    private int SensorName;





    private Smart_mirror smart_mirror;


    public Sensor(
        int SensorID,        int SensorName    ) {
        this.SensorID = SensorID;
        this.SensorName = SensorName;
    }


    public int getSensorid() {
        return SensorID;
    }

    public void setSensorid(int SensorID) {
        this.SensorID = SensorID;
    }
    public int getSensorname() {
        return SensorName;
    }

    public void setSensorname(int SensorName) {
        this.SensorName = SensorName;
    }

    public Smart_mirror getSmart_mirror() {
        return smart_mirror;
    }

    public void setSmart_mirror(Smart_mirror smart_mirror) {
        this.smart_mirror = smart_mirror;
    }

}