





import java.util.List;
import java.util.ArrayList;

public class smoke_sensor  {

    private int smoke_sensor_id;
    private boolean smoke_sensor_status;
    private String smoke_sensor_location;
    private boolean smoke_level_breach;



    public smoke_sensor(
        int smoke_sensor_id,        boolean smoke_sensor_status,        String smoke_sensor_location,        boolean smoke_level_breach    ) {
        this.smoke_sensor_id = smoke_sensor_id;
        this.smoke_sensor_status = smoke_sensor_status;
        this.smoke_sensor_location = smoke_sensor_location;
        this.smoke_level_breach = smoke_level_breach;
    }


    public int getSmoke_sensor_id() {
        return smoke_sensor_id;
    }

    public void setSmoke_sensor_id(int smoke_sensor_id) {
        this.smoke_sensor_id = smoke_sensor_id;
    }
    public boolean getSmoke_sensor_status() {
        return smoke_sensor_status;
    }

    public void setSmoke_sensor_status(boolean smoke_sensor_status) {
        this.smoke_sensor_status = smoke_sensor_status;
    }
    public String getSmoke_sensor_location() {
        return smoke_sensor_location;
    }

    public void setSmoke_sensor_location(String smoke_sensor_location) {
        this.smoke_sensor_location = smoke_sensor_location;
    }
    public boolean getSmoke_level_breach() {
        return smoke_level_breach;
    }

    public void setSmoke_level_breach(boolean smoke_level_breach) {
        this.smoke_level_breach = smoke_level_breach;
    }


}