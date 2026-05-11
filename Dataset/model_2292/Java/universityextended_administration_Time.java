





import java.util.List;
import java.util.ArrayList;

public class universityextended_administration_Time  {

    private int endHour;
    private String day;
    private int startHour;



    public universityextended_administration_Time(
        int endHour,        String day,        int startHour    ) {
        this.endHour = endHour;
        this.day = day;
        this.startHour = startHour;
    }


    public int getEndhour() {
        return endHour;
    }

    public void setEndhour(int endHour) {
        this.endHour = endHour;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
    public int getStarthour() {
        return startHour;
    }

    public void setStarthour(int startHour) {
        this.startHour = startHour;
    }


}