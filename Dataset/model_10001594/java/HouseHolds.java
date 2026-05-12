





import java.util.List;
import java.util.ArrayList;

public class HouseHolds  {

    private String WashingMachine;
    private String Alarm;
    private String TimeID;
    private String Coffee;
    private String DishWasher;





    private IOT iot;




    private End_Of_Day end_of_day;




    private Start_Of_Day start_of_day;


    public HouseHolds(
        String WashingMachine,        String Alarm,        String TimeID,        String Coffee,        String DishWasher    ) {
        this.WashingMachine = WashingMachine;
        this.Alarm = Alarm;
        this.TimeID = TimeID;
        this.Coffee = Coffee;
        this.DishWasher = DishWasher;
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
    public String getDishwasher() {
        return DishWasher;
    }

    public void setDishwasher(String DishWasher) {
        this.DishWasher = DishWasher;
    }

    public IOT getIot() {
        return iot;
    }

    public void setIot(IOT iot) {
        this.iot = iot;
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