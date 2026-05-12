





import java.util.List;
import java.util.ArrayList;

public class appointment  {

    private String title;
    private int day;
    private int minute;
    private int duration;
    private int hour;



    public appointment(
        String title,        int day,        int minute,        int duration,        int hour    ) {
        this.title = title;
        this.day = day;
        this.minute = minute;
        this.duration = duration;
        this.hour = hour;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }
    public int getMinute() {
        return minute;
    }

    public void setMinute(int minute) {
        this.minute = minute;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public int getHour() {
        return hour;
    }

    public void setHour(int hour) {
        this.hour = hour;
    }


}