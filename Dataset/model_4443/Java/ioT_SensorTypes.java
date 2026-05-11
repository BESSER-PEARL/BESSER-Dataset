





import java.util.List;
import java.util.ArrayList;

public class ioT_SensorTypes  {






    private List<ioT_SensorType> iot_sensortypes;


    public ioT_SensorTypes(
    ) {
        this.iot_sensortypes = new ArrayList<>();
    }

    public ioT_SensorTypes(
        ArrayList<ioT_SensorType> iot_sensortypes    ) {
        this.iot_sensortypes = iot_sensortypes;
    }


    public List<ioT_SensorType> getIot_sensortypes() {
        return iot_sensortypes;
    }

    public void addIot_sensortype(Iot_sensortype iot_sensortype) {
        this.iot_sensortypes.add(iot_sensortype);
    }

}