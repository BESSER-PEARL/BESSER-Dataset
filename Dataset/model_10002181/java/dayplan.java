





import java.util.List;
import java.util.ArrayList;

public class dayplan  {

    private String sunday;
    private String thursday;
    private String Monday;
    private String plan_per_date;
    private String tuesday;
    private String wenesday;
    private String saturday;
    private String friday;



    public dayplan(
        String sunday,        String thursday,        String Monday,        String plan_per_date,        String tuesday,        String wenesday,        String saturday,        String friday    ) {
        this.sunday = sunday;
        this.thursday = thursday;
        this.Monday = Monday;
        this.plan_per_date = plan_per_date;
        this.tuesday = tuesday;
        this.wenesday = wenesday;
        this.saturday = saturday;
        this.friday = friday;
    }


    public String getSunday() {
        return sunday;
    }

    public void setSunday(String sunday) {
        this.sunday = sunday;
    }
    public String getThursday() {
        return thursday;
    }

    public void setThursday(String thursday) {
        this.thursday = thursday;
    }
    public String getMonday() {
        return Monday;
    }

    public void setMonday(String Monday) {
        this.Monday = Monday;
    }
    public String getPlan_per_date() {
        return plan_per_date;
    }

    public void setPlan_per_date(String plan_per_date) {
        this.plan_per_date = plan_per_date;
    }
    public String getTuesday() {
        return tuesday;
    }

    public void setTuesday(String tuesday) {
        this.tuesday = tuesday;
    }
    public String getWenesday() {
        return wenesday;
    }

    public void setWenesday(String wenesday) {
        this.wenesday = wenesday;
    }
    public String getSaturday() {
        return saturday;
    }

    public void setSaturday(String saturday) {
        this.saturday = saturday;
    }
    public String getFriday() {
        return friday;
    }

    public void setFriday(String friday) {
        this.friday = friday;
    }


}