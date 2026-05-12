





import java.util.List;
import java.util.ArrayList;

public class PowerSystem  {

    private int DeviceID;





    private System system;


    public PowerSystem(
        int DeviceID    ) {
        this.DeviceID = DeviceID;
    }


    public int getDeviceid() {
        return DeviceID;
    }

    public void setDeviceid(int DeviceID) {
        this.DeviceID = DeviceID;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}