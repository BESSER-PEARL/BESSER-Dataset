





import java.util.List;
import java.util.ArrayList;

public class Light_Sensor  {

    private String Sensor_ID;





    private Camera_1 camera_1;


    public Light_Sensor(
        String Sensor_ID    ) {
        this.Sensor_ID = Sensor_ID;
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

}