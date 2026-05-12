





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_DateTimeType  {

    private String month;
    private String hour;
    private String day;
    private String year;
    private String minute;
    private String second;



    public DatadiagramMLBasicDef_DateTimeType(
        String month,        String hour,        String day,        String year,        String minute,        String second    ) {
        this.month = month;
        this.hour = hour;
        this.day = day;
        this.year = year;
        this.minute = minute;
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


}