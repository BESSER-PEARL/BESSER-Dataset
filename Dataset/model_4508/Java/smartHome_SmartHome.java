





import java.util.List;
import java.util.ArrayList;

public class smartHome_SmartHome  {






    private List<smartHome_SensorType> smarthome_sensortypes;


    public smartHome_SmartHome(
    ) {
        this.smarthome_sensortypes = new ArrayList<>();
    }

    public smartHome_SmartHome(
        ArrayList<smartHome_SensorType> smarthome_sensortypes    ) {
        this.smarthome_sensortypes = smarthome_sensortypes;
    }


    public List<smartHome_SensorType> getSmarthome_sensortypes() {
        return smarthome_sensortypes;
    }

    public void addSmarthome_sensortype(Smarthome_sensortype smarthome_sensortype) {
        this.smarthome_sensortypes.add(smarthome_sensortype);
    }

}