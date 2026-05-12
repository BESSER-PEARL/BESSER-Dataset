





import java.util.List;
import java.util.ArrayList;

public class SolarPanel  {

    private int SPID;





    private IoT_based_Smart_Resort_System iot_based_smart_resort_system;


    public SolarPanel(
        int SPID    ) {
        this.SPID = SPID;
    }


    public int getSpid() {
        return SPID;
    }

    public void setSpid(int SPID) {
        this.SPID = SPID;
    }

    public IoT_based_Smart_Resort_System getIot_based_smart_resort_system() {
        return iot_based_smart_resort_system;
    }

    public void setIot_based_smart_resort_system(IoT_based_Smart_Resort_System iot_based_smart_resort_system) {
        this.iot_based_smart_resort_system = iot_based_smart_resort_system;
    }

}