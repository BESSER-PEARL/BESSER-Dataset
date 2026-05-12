





import java.util.List;
import java.util.ArrayList;

public class HouseHolds  {

    private String TimeID;
    private String Coffee;
    private String WashingMachine;
    private String Alarm;
    private String DishWasher;





    private System system;




    private Start_Of_Day start_of_day;




    private End_Of_Day end_of_day;


    public HouseHolds(
        String TimeID,        String Coffee,        String WashingMachine,        String Alarm,        String DishWasher    ) {
        this.TimeID = TimeID;
        this.Coffee = Coffee;
        this.WashingMachine = WashingMachine;
        this.Alarm = Alarm;
        this.DishWasher = DishWasher;
    }


    public String getTimeid() {
        return TimeID;
    }

    public void setTimeid(String TimeID) {
        this.TimeID = TimeID;
    }
    public String getCoffee() {
        return Coffee;
    }

    public void setCoffee(String Coffee) {
        this.Coffee = Coffee;
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
    public String getDishwasher() {
        return DishWasher;
    }

    public void setDishwasher(String DishWasher) {
        this.DishWasher = DishWasher;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }
    public Start_Of_Day getStart_of_day() {
        return start_of_day;
    }

    public void setStart_of_day(Start_Of_Day start_of_day) {
        this.start_of_day = start_of_day;
    }
    public End_Of_Day getEnd_of_day() {
        return end_of_day;
    }

    public void setEnd_of_day(End_Of_Day end_of_day) {
        this.end_of_day = end_of_day;
    }

}