





import java.util.List;
import java.util.ArrayList;

public class Temperature_sensor  {

    private String Temp_ID;





    private Camera_1 camera_1;


    public Temperature_sensor(
        String Temp_ID    ) {
        this.Temp_ID = Temp_ID;
    }


    public String getTemp_id() {
        return Temp_ID;
    }

    public void setTemp_id(String Temp_ID) {
        this.Temp_ID = Temp_ID;
    }

    public Camera_1 getCamera_1() {
        return camera_1;
    }

    public void setCamera_1(Camera_1 camera_1) {
        this.camera_1 = camera_1;
    }

}