





import java.util.List;
import java.util.ArrayList;

public class events_Timewindow  {

    private String time;





    private events_ComplexEventPattern events_complexeventpattern;


    public events_Timewindow(
        String time    ) {
        this.time = time;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public events_ComplexEventPattern getEvents_complexeventpattern() {
        return events_complexeventpattern;
    }

    public void setEvents_complexeventpattern(events_ComplexEventPattern events_complexeventpattern) {
        this.events_complexeventpattern = events_complexeventpattern;
    }

}