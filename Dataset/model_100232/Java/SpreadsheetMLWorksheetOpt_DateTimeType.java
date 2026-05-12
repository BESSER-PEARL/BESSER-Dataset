





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorksheetOpt_DateTimeType  {

    private String minute;
    private String month;
    private String day;
    private String second;
    private String hour;
    private String year;



    public SpreadsheetMLWorksheetOpt_DateTimeType(
        String minute,        String month,        String day,        String second,        String hour,        String year    ) {
        this.minute = minute;
        this.month = month;
        this.day = day;
        this.second = second;
        this.hour = hour;
        this.year = year;
    }


    public String getMinute() {
        return minute;
    }

    public void setMinute(String minute) {
        this.minute = minute;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getSecond() {
        return second;
    }

    public void setSecond(String second) {
        this.second = second;
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