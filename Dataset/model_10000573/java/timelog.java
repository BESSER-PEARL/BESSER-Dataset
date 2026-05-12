





import java.util.List;
import java.util.ArrayList;

public class timelog  {

    private int seconds;
    private int year;
    private int month;
    private int hour;
    private int minutes;
    private int day;





    private Notification_System notification_system;




    private eventlog eventlog;


    public timelog(
        int seconds,        int year,        int month,        int hour,        int minutes,        int day    ) {
        this.seconds = seconds;
        this.year = year;
        this.month = month;
        this.hour = hour;
        this.minutes = minutes;
        this.day = day;
    }


    public int getSeconds() {
        return seconds;
    }

    public void setSeconds(int seconds) {
        this.seconds = seconds;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        this.month = month;
    }
    public int getHour() {
        return hour;
    }

    public void setHour(int hour) {
        this.hour = hour;
    }
    public int getMinutes() {
        return minutes;
    }

    public void setMinutes(int minutes) {
        this.minutes = minutes;
    }
    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }

    public Notification_System getNotification_system() {
        return notification_system;
    }

    public void setNotification_system(Notification_System notification_system) {
        this.notification_system = notification_system;
    }
    public eventlog getEventlog() {
        return eventlog;
    }

    public void setEventlog(eventlog eventlog) {
        this.eventlog = eventlog;
    }

}