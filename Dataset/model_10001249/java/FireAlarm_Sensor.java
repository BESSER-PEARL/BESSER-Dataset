





import java.util.List;
import java.util.ArrayList;

public class FireAlarm_Sensor  {

    private boolean SmokeAlarm;



    public FireAlarm_Sensor(
        boolean SmokeAlarm    ) {
        this.SmokeAlarm = SmokeAlarm;
    }


    public boolean getSmokealarm() {
        return SmokeAlarm;
    }

    public void setSmokealarm(boolean SmokeAlarm) {
        this.SmokeAlarm = SmokeAlarm;
    }


}