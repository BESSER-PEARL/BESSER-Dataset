





import java.util.List;
import java.util.ArrayList;

public class flood_sensor  {

    private String flood_sensor_loaction;
    private boolean waterlevel_breach_status;
    private int flood_sensor_id;
    private boolean flood_sensor_status;



    public flood_sensor(
        String flood_sensor_loaction,        boolean waterlevel_breach_status,        int flood_sensor_id,        boolean flood_sensor_status    ) {
        this.flood_sensor_loaction = flood_sensor_loaction;
        this.waterlevel_breach_status = waterlevel_breach_status;
        this.flood_sensor_id = flood_sensor_id;
        this.flood_sensor_status = flood_sensor_status;
    }


    public String getFlood_sensor_loaction() {
        return flood_sensor_loaction;
    }

    public void setFlood_sensor_loaction(String flood_sensor_loaction) {
        this.flood_sensor_loaction = flood_sensor_loaction;
    }
    public boolean getWaterlevel_breach_status() {
        return waterlevel_breach_status;
    }

    public void setWaterlevel_breach_status(boolean waterlevel_breach_status) {
        this.waterlevel_breach_status = waterlevel_breach_status;
    }
    public int getFlood_sensor_id() {
        return flood_sensor_id;
    }

    public void setFlood_sensor_id(int flood_sensor_id) {
        this.flood_sensor_id = flood_sensor_id;
    }
    public boolean getFlood_sensor_status() {
        return flood_sensor_status;
    }

    public void setFlood_sensor_status(boolean flood_sensor_status) {
        this.flood_sensor_status = flood_sensor_status;
    }


}