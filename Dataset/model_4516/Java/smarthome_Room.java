





import java.util.List;
import java.util.ArrayList;

public class smarthome_Room extends NamedEntity {






    private List<smarthome_Sensor> smarthome_sensors;


    public smarthome_Room(
    ) {
        super(
        );
        this.smarthome_sensors = new ArrayList<>();
    }

    public smarthome_Room(
        ArrayList<smarthome_Sensor> smarthome_sensors    ) {
        this.smarthome_sensors = smarthome_sensors;
    }


    public List<smarthome_Sensor> getSmarthome_sensors() {
        return smarthome_sensors;
    }

    public void addSmarthome_sensor(Smarthome_sensor smarthome_sensor) {
        this.smarthome_sensors.add(smarthome_sensor);
    }

}