





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_DateTimeType  {

    private String minute;
    private String second;
    private String day;
    private String month;
    private String hour;
    private String year;



    public SpreadsheetMLSimplified_DateTimeType(
        String minute,        String second,        String day,        String month,        String hour,        String year    ) {
        this.minute = minute;
        this.second = second;
        this.day = day;
        this.month = month;
        this.hour = hour;
        this.year = year;
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
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
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
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }


}