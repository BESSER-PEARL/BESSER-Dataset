





import java.util.List;
import java.util.ArrayList;

public class Camera_1  {

    private String Camera_ID;
    private String Sensor_ID;





    private Camera_1 camera_1;




    private Home_Security__Hub_ home_security__hub_;


    public Camera_1(
        String Camera_ID,        String Sensor_ID    ) {
        this.Camera_ID = Camera_ID;
        this.Sensor_ID = Sensor_ID;
    }


    public String getCamera_id() {
        return Camera_ID;
    }

    public void setCamera_id(String Camera_ID) {
        this.Camera_ID = Camera_ID;
    }
    public String getSensor_id() {
        return Sensor_ID;
    }

    public void setSensor_id(String Sensor_ID) {
        this.Sensor_ID = Sensor_ID;
    }

    public Camera_1 getCamera_1() {
        return camera_1;
    }

    public void setCamera_1(Camera_1 camera_1) {
        this.camera_1 = camera_1;
    }
    public Home_Security__Hub_ getHome_security__hub_() {
        return home_security__hub_;
    }

    public void setHome_security__hub_(Home_Security__Hub_ home_security__hub_) {
        this.home_security__hub_ = home_security__hub_;
    }

}