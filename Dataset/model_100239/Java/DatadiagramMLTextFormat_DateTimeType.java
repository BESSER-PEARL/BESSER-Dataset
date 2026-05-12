





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_DateTimeType  {

    private String minute;
    private String year;
    private String hour;
    private String day;
    private String second;
    private String month;



    public DatadiagramMLTextFormat_DateTimeType(
        String minute,        String year,        String hour,        String day,        String second,        String month    ) {
        this.minute = minute;
        this.year = year;
        this.hour = hour;
        this.day = day;
        this.second = second;
        this.month = month;
    }


    public String getMinute() {
        return minute;
    }

    public void setMinute(String minute) {
        this.minute = minute;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getHour() {
        return hour;
    }

    public void setHour(String hour) {
        this.hour = hour;
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
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }


}