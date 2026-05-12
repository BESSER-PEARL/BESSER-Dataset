





import java.util.List;
import java.util.ArrayList;

public class Device_Configuration  {

    private int zone;
    private boolean activeOnAway;
    private boolean alarmIfoff;
    private boolean activeOnStay;



    public Device_Configuration(
        int zone,        boolean activeOnAway,        boolean alarmIfoff,        boolean activeOnStay    ) {
        this.zone = zone;
        this.activeOnAway = activeOnAway;
        this.alarmIfoff = alarmIfoff;
        this.activeOnStay = activeOnStay;
    }


    public int getZone() {
        return zone;
    }

    public void setZone(int zone) {
        this.zone = zone;
    }
    public boolean getActiveonaway() {
        return activeOnAway;
    }

    public void setActiveonaway(boolean activeOnAway) {
        this.activeOnAway = activeOnAway;
    }
    public boolean getAlarmifoff() {
        return alarmIfoff;
    }

    public void setAlarmifoff(boolean alarmIfoff) {
        this.alarmIfoff = alarmIfoff;
    }
    public boolean getActiveonstay() {
        return activeOnStay;
    }

    public void setActiveonstay(boolean activeOnStay) {
        this.activeOnStay = activeOnStay;
    }


}