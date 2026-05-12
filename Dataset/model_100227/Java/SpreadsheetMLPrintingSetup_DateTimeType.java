





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_DateTimeType  {

    private String year;
    private String second;
    private String day;
    private String month;
    private String minute;
    private String hour;



    public SpreadsheetMLPrintingSetup_DateTimeType(
        String year,        String second,        String day,        String month,        String minute,        String hour    ) {
        this.year = year;
        this.second = second;
        this.day = day;
        this.month = month;
        this.minute = minute;
        this.hour = hour;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
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
    public String getMinute() {
        return minute;
    }

    public void setMinute(String minute) {
        this.minute = minute;
    }
    public String getHour() {
        return hour;
    }

    public void setHour(String hour) {
        this.hour = hour;
    }


}