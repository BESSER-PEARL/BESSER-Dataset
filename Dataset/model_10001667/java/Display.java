





import java.util.List;
import java.util.ArrayList;

public class Display  {

    private String Coffee;
    private String TimeID;
    private String DishWasher;
    private String Alarm;
    private String WashingMachine;





    private Hub_Device hub_device;




    private End_Of_Day end_of_day;




    private Start_Of_Day start_of_day;


    public Display(
        String Coffee,        String TimeID,        String DishWasher,        String Alarm,        String WashingMachine    ) {
        this.Coffee = Coffee;
        this.TimeID = TimeID;
        this.DishWasher = DishWasher;
        this.Alarm = Alarm;
        this.WashingMachine = WashingMachine;
    }


    public String getCoffee() {
        return Coffee;
    }

    public void setCoffee(String Coffee) {
        this.Coffee = Coffee;
    }
    public String getTimeid() {
        return TimeID;
    }

    public void setTimeid(String TimeID) {
        this.TimeID = TimeID;
    }
    public String getDishwasher() {
        return DishWasher;
    }

    public void setDishwasher(String DishWasher) {
        this.DishWasher = DishWasher;
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

    public Hub_Device getHub_device() {
        return hub_device;
    }

    public void setHub_device(Hub_Device hub_device) {
        this.hub_device = hub_device;
    }
    public End_Of_Day getEnd_of_day() {
        return end_of_day;
    }

    public void setEnd_of_day(End_Of_Day end_of_day) {
        this.end_of_day = end_of_day;
    }
    public Start_Of_Day getStart_of_day() {
        return start_of_day;
    }

    public void setStart_of_day(Start_Of_Day start_of_day) {
        this.start_of_day = start_of_day;
    }

}