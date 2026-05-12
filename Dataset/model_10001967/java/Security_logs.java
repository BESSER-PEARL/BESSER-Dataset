





import java.util.List;
import java.util.ArrayList;

public class Security_logs  {

    private String Log_ID;
    private String Sensor_ID;
    private String Camera_ID;





    private Home_Security__Hub_ home_security__hub_;


    public Security_logs(
        String Log_ID,        String Sensor_ID,        String Camera_ID    ) {
        this.Log_ID = Log_ID;
        this.Sensor_ID = Sensor_ID;
        this.Camera_ID = Camera_ID;
    }


    public String getLog_id() {
        return Log_ID;
    }

    public void setLog_id(String Log_ID) {
        this.Log_ID = Log_ID;
    }
    public String getSensor_id() {
        return Sensor_ID;
    }

    public void setSensor_id(String Sensor_ID) {
        this.Sensor_ID = Sensor_ID;
    }
    public String getCamera_id() {
        return Camera_ID;
    }

    public void setCamera_id(String Camera_ID) {
        this.Camera_ID = Camera_ID;
    }

    public Home_Security__Hub_ getHome_security__hub_() {
        return home_security__hub_;
    }

    public void setHome_security__hub_(Home_Security__Hub_ home_security__hub_) {
        this.home_security__hub_ = home_security__hub_;
    }

}