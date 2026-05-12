





import java.util.List;
import java.util.ArrayList;

public class Home_Security_System  {

    private int UserID;





    private IoT_based_Smart_Resort_System iot_based_smart_resort_system;


    public Home_Security_System(
        int UserID    ) {
        this.UserID = UserID;
    }


    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }

    public IoT_based_Smart_Resort_System getIot_based_smart_resort_system() {
        return iot_based_smart_resort_system;
    }

    public void setIot_based_smart_resort_system(IoT_based_Smart_Resort_System iot_based_smart_resort_system) {
        this.iot_based_smart_resort_system = iot_based_smart_resort_system;
    }

}