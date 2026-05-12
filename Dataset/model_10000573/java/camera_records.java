





import java.util.List;
import java.util.ArrayList;

public class camera_records  {

    private String camera_location;
    private boolean camera_status_on;
    private int camera_id;



    public camera_records(
        String camera_location,        boolean camera_status_on,        int camera_id    ) {
        this.camera_location = camera_location;
        this.camera_status_on = camera_status_on;
        this.camera_id = camera_id;
    }


    public String getCamera_location() {
        return camera_location;
    }

    public void setCamera_location(String camera_location) {
        this.camera_location = camera_location;
    }
    public boolean getCamera_status_on() {
        return camera_status_on;
    }

    public void setCamera_status_on(boolean camera_status_on) {
        this.camera_status_on = camera_status_on;
    }
    public int getCamera_id() {
        return camera_id;
    }

    public void setCamera_id(int camera_id) {
        this.camera_id = camera_id;
    }


}