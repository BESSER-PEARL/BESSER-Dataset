





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_DateTimeType  {

    private String month;
    private String minute;
    private String second;
    private String year;
    private String day;
    private String hour;



    public SpreadsheetMLSimplified_DateTimeType(
        String month,        String minute,        String second,        String year,        String day,        String hour    ) {
        this.month = month;
        this.minute = minute;
        this.second = second;
        this.year = year;
        this.day = day;
        this.hour = hour;
    }


    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getMinute() {
        return minute;
    }

    public void setMinute(String minute) {
        this.minute = minute;
    }
    public String getSecond() {
        return second;
    }

    public void setSecond(String second) {
        this.second = second;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getHour() {
        return hour;
    }

    public void setHour(String hour) {
        this.hour = hour;
    }


}