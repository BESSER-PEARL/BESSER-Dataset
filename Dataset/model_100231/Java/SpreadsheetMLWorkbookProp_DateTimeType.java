





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorkbookProp_DateTimeType  {

    private String minute;
    private String day;
    private String hour;
    private String second;
    private String year;
    private String month;



    public SpreadsheetMLWorkbookProp_DateTimeType(
        String minute,        String day,        String hour,        String second,        String year,        String month    ) {
        this.minute = minute;
        this.day = day;
        this.hour = hour;
        this.second = second;
        this.year = year;
        this.month = month;
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
    public String getHour() {
        return hour;
    }

    public void setHour(String hour) {
        this.hour = hour;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }


}