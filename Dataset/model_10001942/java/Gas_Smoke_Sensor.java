





import java.util.List;
import java.util.ArrayList;

public class Gas_Smoke_Sensor  {

    private boolean SmokeAlarm;
    private boolean CheckSmoke;



    public Gas_Smoke_Sensor(
        boolean SmokeAlarm,        boolean CheckSmoke    ) {
        this.SmokeAlarm = SmokeAlarm;
        this.CheckSmoke = CheckSmoke;
    }


    public boolean getSmokealarm() {
        return SmokeAlarm;
    }

    public void setSmokealarm(boolean SmokeAlarm) {
        this.SmokeAlarm = SmokeAlarm;
    }
    public boolean getChecksmoke() {
        return CheckSmoke;
    }

    public void setChecksmoke(boolean CheckSmoke) {
        this.CheckSmoke = CheckSmoke;
    }


}