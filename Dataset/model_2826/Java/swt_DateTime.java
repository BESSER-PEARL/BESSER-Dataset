





import java.util.List;
import java.util.ArrayList;

public class swt_DateTime extends Control {

    private int month;
    private int minutes;
    private int seconds;
    private int year;
    private int hours;
    private int day;



    public swt_DateTime(
        int month,        int minutes,        int seconds,        int year,        int hours,        int day    ) {
        super(
        );
        this.month = month;
        this.minutes = minutes;
        this.seconds = seconds;
        this.year = year;
        this.hours = hours;
        this.day = day;
    }


    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        this.month = month;
    }
    public int getMinutes() {
        return minutes;
    }

    public void setMinutes(int minutes) {
        this.minutes = minutes;
    }
    public int getSeconds() {
        return seconds;
    }

    public void setSeconds(int seconds) {
        this.seconds = seconds;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public int getHours() {
        return hours;
    }

    public void setHours(int hours) {
        this.hours = hours;
    }
    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }


}