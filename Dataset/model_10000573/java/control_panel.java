





import java.util.List;
import java.util.ArrayList;

public class control_panel  {

    private boolean system_on;





    private camera_records camera_records;


    public control_panel(
        boolean system_on    ) {
        this.system_on = system_on;
    }


    public boolean getSystem_on() {
        return system_on;
    }

    public void setSystem_on(boolean system_on) {
        this.system_on = system_on;
    }

    public camera_records getCamera_records() {
        return camera_records;
    }

    public void setCamera_records(camera_records camera_records) {
        this.camera_records = camera_records;
    }

}