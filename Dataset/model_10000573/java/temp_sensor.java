





import java.util.List;
import java.util.ArrayList;

public class temp_sensor  {

    private int temp_sensor_id;
    private String temp_sensor_location;
    private boolean temp_level_breach;
    private boolean temp_sensor_status;



    public temp_sensor(
        int temp_sensor_id,        String temp_sensor_location,        boolean temp_level_breach,        boolean temp_sensor_status    ) {
        this.temp_sensor_id = temp_sensor_id;
        this.temp_sensor_location = temp_sensor_location;
        this.temp_level_breach = temp_level_breach;
        this.temp_sensor_status = temp_sensor_status;
    }


    public int getTemp_sensor_id() {
        return temp_sensor_id;
    }

    public void setTemp_sensor_id(int temp_sensor_id) {
        this.temp_sensor_id = temp_sensor_id;
    }
    public String getTemp_sensor_location() {
        return temp_sensor_location;
    }

    public void setTemp_sensor_location(String temp_sensor_location) {
        this.temp_sensor_location = temp_sensor_location;
    }
    public boolean getTemp_level_breach() {
        return temp_level_breach;
    }

    public void setTemp_level_breach(boolean temp_level_breach) {
        this.temp_level_breach = temp_level_breach;
    }
    public boolean getTemp_sensor_status() {
        return temp_sensor_status;
    }

    public void setTemp_sensor_status(boolean temp_sensor_status) {
        this.temp_sensor_status = temp_sensor_status;
    }


}