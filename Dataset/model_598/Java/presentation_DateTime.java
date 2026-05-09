





import java.util.List;
import java.util.ArrayList;

public class presentation_DateTime extends Composite {

    private String minutes;
    private String day;
    private String seconds;
    private String hours;
    private String month;
    private String year;



    public presentation_DateTime(
        String minutes,        String day,        String seconds,        String hours,        String month,        String year    ) {
        super(
        );
        this.minutes = minutes;
        this.day = day;
        this.seconds = seconds;
        this.hours = hours;
        this.month = month;
        this.year = year;
    }


    public String getMinutes() {
        return minutes;
    }

    public void setMinutes(String minutes) {
        this.minutes = minutes;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getSeconds() {
        return seconds;
    }

    public void setSeconds(String seconds) {
        this.seconds = seconds;
    }
    public String getHours() {
        return hours;
    }

    public void setHours(String hours) {
        this.hours = hours;
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


}