





import java.util.List;
import java.util.ArrayList;

public class Sensor  {

    private int SensorID;
    private int SensorType;





    private IoT_based_Smart_Resort_System iot_based_smart_resort_system;


    public Sensor(
        int SensorID,        int SensorType    ) {
        this.SensorID = SensorID;
        this.SensorType = SensorType;
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

    public IoT_based_Smart_Resort_System getIot_based_smart_resort_system() {
        return iot_based_smart_resort_system;
    }

    public void setIot_based_smart_resort_system(IoT_based_Smart_Resort_System iot_based_smart_resort_system) {
        this.iot_based_smart_resort_system = iot_based_smart_resort_system;
    }

}