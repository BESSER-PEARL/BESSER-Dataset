





import java.util.List;
import java.util.ArrayList;

public class Schedule  {

    private String startTime;
    private int scheduleID;
    private String date;
    private boolean available;
    private String endTime;



    public Schedule(
        String startTime,        int scheduleID,        String date,        boolean available,        String endTime    ) {
        this.startTime = startTime;
        this.scheduleID = scheduleID;
        this.date = date;
        this.available = available;
        this.endTime = endTime;
    }


    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public int getScheduleid() {
        return scheduleID;
    }

    public void setScheduleid(int scheduleID) {
        this.scheduleID = scheduleID;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public boolean getAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
    }
    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }


}