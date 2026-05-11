





import java.util.List;
import java.util.ArrayList;

public class wsn_SensorRole extends Lifeline,  {






    private wsn_Sensor wsn_sensor;


    public wsn_SensorRole(
    ) {
        super(
        );
    }



    public wsn_Sensor getWsn_sensor() {
        return wsn_sensor;
    }

    public void setWsn_sensor(wsn_Sensor wsn_sensor) {
        this.wsn_sensor = wsn_sensor;
    }

}