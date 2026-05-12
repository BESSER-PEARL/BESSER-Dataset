





import java.util.List;
import java.util.ArrayList;

public class FireAlarm_Sensor  {

    private boolean SmokeAlarm;
    private boolean DispenseSprinkler;



    public FireAlarm_Sensor(
        boolean SmokeAlarm,        boolean DispenseSprinkler    ) {
        this.SmokeAlarm = SmokeAlarm;
        this.DispenseSprinkler = DispenseSprinkler;
    }


    public boolean getSmokealarm() {
        return SmokeAlarm;
    }

    public void setSmokealarm(boolean SmokeAlarm) {
        this.SmokeAlarm = SmokeAlarm;
    }
    public boolean getDispensesprinkler() {
        return DispenseSprinkler;
    }

    public void setDispensesprinkler(boolean DispenseSprinkler) {
        this.DispenseSprinkler = DispenseSprinkler;
    }


}