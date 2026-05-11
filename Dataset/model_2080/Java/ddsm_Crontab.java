





import java.util.List;
import java.util.ArrayList;

public class ddsm_Crontab  {

    private int month;
    private int min;
    private int dayOfMonth;
    private int hour;
    private int dayOfWeek;





    private ddsm_ClientNode ddsm_clientnode;


    public ddsm_Crontab(
        int month,        int min,        int dayOfMonth,        int hour,        int dayOfWeek    ) {
        this.month = month;
        this.min = min;
        this.dayOfMonth = dayOfMonth;
        this.hour = hour;
        this.dayOfWeek = dayOfWeek;
    }


    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        this.month = month;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getDayofmonth() {
        return dayOfMonth;
    }

    public void setDayofmonth(int dayOfMonth) {
        this.dayOfMonth = dayOfMonth;
    }
    public int getHour() {
        return hour;
    }

    public void setHour(int hour) {
        this.hour = hour;
    }
    public int getDayofweek() {
        return dayOfWeek;
    }

    public void setDayofweek(int dayOfWeek) {
        this.dayOfWeek = dayOfWeek;
    }

    public ddsm_ClientNode getDdsm_clientnode() {
        return ddsm_clientnode;
    }

    public void setDdsm_clientnode(ddsm_ClientNode ddsm_clientnode) {
        this.ddsm_clientnode = ddsm_clientnode;
    }

}