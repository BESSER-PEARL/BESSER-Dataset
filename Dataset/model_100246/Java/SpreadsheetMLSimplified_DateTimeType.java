





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_DateTimeType  {

    private int day;
    private int minute;
    private int second;
    private int hour;
    private int year;
    private int month;



    public SpreadsheetMLSimplified_DateTimeType(
        int day,        int minute,        int second,        int hour,        int year,        int month    ) {
        this.day = day;
        this.minute = minute;
        this.second = second;
        this.hour = hour;
        this.year = year;
        this.month = month;
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
    public int getSecond() {
        return second;
    }

    public void setSecond(int second) {
        this.second = second;
    }
    public int getHour() {
        return hour;
    }

    public void setHour(int hour) {
        this.hour = hour;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        this.month = month;
    }


}