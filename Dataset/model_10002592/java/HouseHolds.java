





import java.util.List;
import java.util.ArrayList;

public class HouseHolds  {

    private String Coffee;
    private String DishWasher;
    private String TimeID;
    private String WashingMachine;
    private String Alarm;





    private System system;


    public HouseHolds(
        String Coffee,        String DishWasher,        String TimeID,        String WashingMachine,        String Alarm    ) {
        this.Coffee = Coffee;
        this.DishWasher = DishWasher;
        this.TimeID = TimeID;
        this.WashingMachine = WashingMachine;
        this.Alarm = Alarm;
    }


    public String getCoffee() {
        return Coffee;
    }

    public void setCoffee(String Coffee) {
        this.Coffee = Coffee;
    }
    public String getDishwasher() {
        return DishWasher;
    }

    public void setDishwasher(String DishWasher) {
        this.DishWasher = DishWasher;
    }
    public String getTimeid() {
        return TimeID;
    }

    public void setTimeid(String TimeID) {
        this.TimeID = TimeID;
    }
    public String getWashingmachine() {
        return WashingMachine;
    }

    public void setWashingmachine(String WashingMachine) {
        this.WashingMachine = WashingMachine;
    }
    public String getAlarm() {
        return Alarm;
    }

    public void setAlarm(String Alarm) {
        this.Alarm = Alarm;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}