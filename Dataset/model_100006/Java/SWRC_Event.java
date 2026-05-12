





import java.util.List;
import java.util.ArrayList;

public class SWRC_Event  {

    private String date;
    private String eventTitle;
    private String location;
    private String name;



    public SWRC_Event(
        String date,        String eventTitle,        String location,        String name    ) {
        this.date = date;
        this.eventTitle = eventTitle;
        this.location = location;
        this.name = name;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getEventtitle() {
        return eventTitle;
    }

    public void setEventtitle(String eventTitle) {
        this.eventTitle = eventTitle;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}