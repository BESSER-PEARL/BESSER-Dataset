





import java.util.List;
import java.util.ArrayList;

public class Home_Security__Hub_  {

    private String Camera_ID;
    private String Login_ID;
    private String Hub_ID;
    private String Sensor_ID;



    public Home_Security__Hub_(
        String Camera_ID,        String Login_ID,        String Hub_ID,        String Sensor_ID    ) {
        this.Camera_ID = Camera_ID;
        this.Login_ID = Login_ID;
        this.Hub_ID = Hub_ID;
        this.Sensor_ID = Sensor_ID;
    }


    public String getCamera_id() {
        return Camera_ID;
    }

    public void setCamera_id(String Camera_ID) {
        this.Camera_ID = Camera_ID;
    }
    public String getLogin_id() {
        return Login_ID;
    }

    public void setLogin_id(String Login_ID) {
        this.Login_ID = Login_ID;
    }
    public String getHub_id() {
        return Hub_ID;
    }

    public void setHub_id(String Hub_ID) {
        this.Hub_ID = Hub_ID;
    }
    public String getSensor_id() {
        return Sensor_ID;
    }

    public void setSensor_id(String Sensor_ID) {
        this.Sensor_ID = Sensor_ID;
    }


}