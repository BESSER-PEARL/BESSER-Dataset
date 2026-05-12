





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_DateTimeType  {

    private String second;
    private String month;
    private String hour;
    private String minute;
    private String day;
    private String year;



    public SpreadsheetMLStyles_DateTimeType(
        String second,        String month,        String hour,        String minute,        String day,        String year    ) {
        this.second = second;
        this.month = month;
        this.hour = hour;
        this.minute = minute;
        this.day = day;
        this.year = year;
    }


    public String getSecond() {
        return second;
    }

    public void setSecond(String second) {
        this.second = second;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getHour() {
        return hour;
    }

    public void setHour(String hour) {
        this.hour = hour;
    }
    public String getMinute() {
        return minute;
    }

    public void setMinute(String minute) {
        this.minute = minute;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }


}