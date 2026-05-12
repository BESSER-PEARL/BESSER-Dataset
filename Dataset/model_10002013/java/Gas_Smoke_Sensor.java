





import java.util.List;
import java.util.ArrayList;

public class Gas_Smoke_Sensor  {

    private boolean DispenseSprinkler;
    private boolean SmokeAlarm;



    public Gas_Smoke_Sensor(
        boolean DispenseSprinkler,        boolean SmokeAlarm    ) {
        this.DispenseSprinkler = DispenseSprinkler;
        this.SmokeAlarm = SmokeAlarm;
    }


    public boolean getDispensesprinkler() {
        return DispenseSprinkler;
    }

    public void setDispensesprinkler(boolean DispenseSprinkler) {
        this.DispenseSprinkler = DispenseSprinkler;
    }
    public boolean getSmokealarm() {
        return SmokeAlarm;
    }

    public void setSmokealarm(boolean SmokeAlarm) {
        this.SmokeAlarm = SmokeAlarm;
    }


}