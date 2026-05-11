





import java.util.List;
import java.util.ArrayList;

public class form_DurationFormField extends ItemContainer, SingleValuatedFormField {

    private String hour;
    private String sec;
    private String day;
    private String min;



    public form_DurationFormField(
        String hour,        String sec,        String day,        String min    ) {
        super(
        );
        this.hour = hour;
        this.sec = sec;
        this.day = day;
        this.min = min;
    }


    public String getHour() {
        return hour;
    }

    public void setHour(String hour) {
        this.hour = hour;
    }
    public String getSec() {
        return sec;
    }

    public void setSec(String sec) {
        this.sec = sec;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }


}