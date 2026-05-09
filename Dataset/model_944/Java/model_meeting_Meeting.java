




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_meeting_Meeting extends UnicaseModelElement {

    private LocalDate starttime;
    private LocalDate endtime;
    private String location;



    public model_meeting_Meeting(
        LocalDate starttime,        LocalDate endtime,        String location    ) {
        super(
        );
        this.starttime = starttime;
        this.endtime = endtime;
        this.location = location;
    }


    public LocalDate getStarttime() {
        return starttime;
    }

    public void setStarttime(LocalDate starttime) {
        this.starttime = starttime;
    }
    public LocalDate getEndtime() {
        return endtime;
    }

    public void setEndtime(LocalDate endtime) {
        this.endtime = endtime;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}