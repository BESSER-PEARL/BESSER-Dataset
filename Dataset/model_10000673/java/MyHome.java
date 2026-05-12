





import java.util.List;
import java.util.ArrayList;

public class MyHome  {

    private String Alarm;
    private String WashingMachine;
    private String TimeID;
    private String Coffee;
    private String DishWasher;





    private Morning morning;




    private Evening evening;


    public MyHome(
        String Alarm,        String WashingMachine,        String TimeID,        String Coffee,        String DishWasher    ) {
        this.Alarm = Alarm;
        this.WashingMachine = WashingMachine;
        this.TimeID = TimeID;
        this.Coffee = Coffee;
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

    public Morning getMorning() {
        return morning;
    }

    public void setMorning(Morning morning) {
        this.morning = morning;
    }
    public Evening getEvening() {
        return evening;
    }

    public void setEvening(Evening evening) {
        this.evening = evening;
    }

}