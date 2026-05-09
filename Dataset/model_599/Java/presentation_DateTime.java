





import java.util.List;
import java.util.ArrayList;

public class presentation_DateTime extends Composite {

    private String seconds;
    private String minutes;
    private String month;
    private String hours;
    private String year;
    private String day;



    public presentation_DateTime(
        String seconds,        String minutes,        String month,        String hours,        String year,        String day    ) {
        super(
        );
        this.seconds = seconds;
        this.minutes = minutes;
        this.month = month;
        this.hours = hours;
        this.year = year;
        this.day = day;
    }


    public String getSeconds() {
        return seconds;
    }

    public void setSeconds(String seconds) {
        this.seconds = seconds;
    }
    public String getMinutes() {
        return minutes;
    }

    public void setMinutes(String minutes) {
        this.minutes = minutes;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getHours() {
        return hours;
    }

    public void setHours(String hours) {
        this.hours = hours;
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


}