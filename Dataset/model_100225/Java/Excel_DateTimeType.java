





import java.util.List;
import java.util.ArrayList;

public class Excel_DateTimeType  {

    private String hour;
    private String month;
    private String year;
    private String day;
    private String second;
    private String minute;



    public Excel_DateTimeType(
        String hour,        String month,        String year,        String day,        String second,        String minute    ) {
        this.hour = hour;
        this.month = month;
        this.year = year;
        this.day = day;
        this.second = second;
        this.minute = minute;
    }


    public String getHour() {
        return hour;
    }

    public void setHour(String hour) {
        this.hour = hour;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
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
    public String getSecond() {
        return second;
    }

    public void setSecond(String second) {
        this.second = second;
    }
    public String getMinute() {
        return minute;
    }

    public void setMinute(String minute) {
        this.minute = minute;
    }


}