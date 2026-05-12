





import java.util.List;
import java.util.ArrayList;

public class door_sensor  {

    private String door_location;
    private int door_sensor_id;
    private boolean door_open_status;



    public door_sensor(
        String door_location,        int door_sensor_id,        boolean door_open_status    ) {
        this.door_location = door_location;
        this.door_sensor_id = door_sensor_id;
        this.door_open_status = door_open_status;
    }


    public String getDoor_location() {
        return door_location;
    }

    public void setDoor_location(String door_location) {
        this.door_location = door_location;
    }
    public int getDoor_sensor_id() {
        return door_sensor_id;
    }

    public void setDoor_sensor_id(int door_sensor_id) {
        this.door_sensor_id = door_sensor_id;
    }
    public boolean getDoor_open_status() {
        return door_open_status;
    }

    public void setDoor_open_status(boolean door_open_status) {
        this.door_open_status = door_open_status;
    }


}