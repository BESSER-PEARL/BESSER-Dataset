





import java.util.List;
import java.util.ArrayList;

public class wsn_SensingAction extends , Action {

    private String sensorId;
    private String data;



    public wsn_SensingAction(
        String sensorId,        String data    ) {
        super(
        );
        this.sensorId = sensorId;
        this.data = data;
    }


    public String getSensorid() {
        return sensorId;
    }

    public void setSensorid(String sensorId) {
        this.sensorId = sensorId;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}