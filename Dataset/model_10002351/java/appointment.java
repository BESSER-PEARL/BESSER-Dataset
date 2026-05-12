





import java.util.List;
import java.util.ArrayList;

public class appointment  {

    private int duration;
    private int minute;
    private int hour;
    private int day;



    public appointment(
        int duration,        int minute,        int hour,        int day    ) {
        this.duration = duration;
        this.minute = minute;
        this.hour = hour;
        this.day = day;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public int getMinute() {
        return minute;
    }

    public void setMinute(int minute) {
        this.minute = minute;
    }
    public int getHour() {
        return hour;
    }

    public void setHour(int hour) {
        this.hour = hour;
    }
    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }


}