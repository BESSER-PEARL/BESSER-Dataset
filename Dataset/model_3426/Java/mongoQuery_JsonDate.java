





import java.util.List;
import java.util.ArrayList;

public class mongoQuery_JsonDate  {

    private int second;
    private int milliseconds;
    private int minute;
    private int month;
    private int year;
    private String dateString;
    private int millisecond;
    private int hour;
    private int day;





    private mongoQuery_Query mongoquery_query;


    public mongoQuery_JsonDate(
        int second,        int milliseconds,        int minute,        int month,        int year,        String dateString,        int millisecond,        int hour,        int day    ) {
        this.second = second;
        this.milliseconds = milliseconds;
        this.minute = minute;
        this.month = month;
        this.year = year;
        this.dateString = dateString;
        this.millisecond = millisecond;
        this.hour = hour;
        this.day = day;
    }


    public int getSecond() {
        return second;
    }

    public void setSecond(int second) {
        this.second = second;
    }
    public int getMilliseconds() {
        return milliseconds;
    }

    public void setMilliseconds(int milliseconds) {
        this.milliseconds = milliseconds;
    }
    public int getMinute() {
        return minute;
    }

    public void setMinute(int minute) {
        this.minute = minute;
    }
    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        this.month = month;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getDatestring() {
        return dateString;
    }

    public void setDatestring(String dateString) {
        this.dateString = dateString;
    }
    public int getMillisecond() {
        return millisecond;
    }

    public void setMillisecond(int millisecond) {
        this.millisecond = millisecond;
    }
    public int getHour() {
        return hour;
    }

    public void setHour(int hour) {
        this.hour = hour;
    }
    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        this.day = day;
    }

    public mongoQuery_Query getMongoquery_query() {
        return mongoquery_query;
    }

    public void setMongoquery_query(mongoQuery_Query mongoquery_query) {
        this.mongoquery_query = mongoquery_query;
    }

}