




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_meeting_Meeting extends UnicaseModelElement {

    private String location;
    private LocalDate endtime;
    private LocalDate starttime;



    public model_meeting_Meeting(
        String location,        LocalDate endtime,        LocalDate starttime    ) {
        super(
        );
        this.location = location;
        this.endtime = endtime;
        this.starttime = starttime;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public LocalDate getEndtime() {
        return endtime;
    }

    public void setEndtime(LocalDate endtime) {
        this.endtime = endtime;
    }
    public LocalDate getStarttime() {
        return starttime;
    }

    public void setStarttime(LocalDate starttime) {
        this.starttime = starttime;
    }


}