





import java.util.List;
import java.util.ArrayList;

public class HouseHolds  {

    private String TimeID;
    private String Alarm;
    private String WashingMachine;





    private System system;


    public HouseHolds(
        String TimeID,        String Alarm,        String WashingMachine    ) {
        this.TimeID = TimeID;
        this.Alarm = Alarm;
        this.WashingMachine = WashingMachine;
    }


    public String getTimeid() {
        return TimeID;
    }

    public void setTimeid(String TimeID) {
        this.TimeID = TimeID;
    }
    public String getAlarm() {
        return Alarm;
    }

    public void setAlarm(String Alarm) {
        this.Alarm = Alarm;
    }
    public String getWashingmachine() {
        return WashingMachine;
    }

    public void setWashingmachine(String WashingMachine) {
        this.WashingMachine = WashingMachine;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}