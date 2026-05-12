





import java.util.List;
import java.util.ArrayList;

public class smokeAlarm  {

    private boolean status;





    private Fire_Alarm_system fire_alarm_system;


    public smokeAlarm(
        boolean status    ) {
        this.status = status;
    }


    public boolean getStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public Fire_Alarm_system getFire_alarm_system() {
        return fire_alarm_system;
    }

    public void setFire_alarm_system(Fire_Alarm_system fire_alarm_system) {
        this.fire_alarm_system = fire_alarm_system;
    }

}