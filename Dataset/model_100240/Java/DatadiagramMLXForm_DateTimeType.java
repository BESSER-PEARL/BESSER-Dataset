





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_DateTimeType  {

    private String year;
    private String month;
    private String second;
    private String day;
    private String hour;
    private String minute;



    public DatadiagramMLXForm_DateTimeType(
        String year,        String month,        String second,        String day,        String hour,        String minute    ) {
        this.year = year;
        this.month = month;
        this.second = second;
        this.day = day;
        this.hour = hour;
        this.minute = minute;
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


}