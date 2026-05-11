





import java.util.List;
import java.util.ArrayList;

public class smartHome_SmartHome  {






    private List<smartHome_SensorType> smarthome_sensortypes;




    private List<smartHome_Location> smarthome_locations;


    public smartHome_SmartHome(
    ) {
        this.smarthome_sensortypes = new ArrayList<>();
        this.smarthome_locations = new ArrayList<>();
    }

    public smartHome_SmartHome(
        ArrayList<smartHome_SensorType> smarthome_sensortypes,        ArrayList<smartHome_Location> smarthome_locations    ) {
        this.smarthome_sensortypes = smarthome_sensortypes;
        this.smarthome_locations = smarthome_locations;
    }


    public List<smartHome_SensorType> getSmarthome_sensortypes() {
        return smarthome_sensortypes;
    }

    public void addSmarthome_sensortype(Smarthome_sensortype smarthome_sensortype) {
        this.smarthome_sensortypes.add(smarthome_sensortype);
    }
    public List<smartHome_Location> getSmarthome_locations() {
        return smarthome_locations;
    }

    public void addSmarthome_location(Smarthome_location smarthome_location) {
        this.smarthome_locations.add(smarthome_location);
    }

}