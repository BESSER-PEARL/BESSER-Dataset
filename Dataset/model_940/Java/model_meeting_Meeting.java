




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_meeting_Meeting extends UnicaseModelElement {

    private LocalDate starttime;
    private String location;
    private LocalDate endtime;



    public model_meeting_Meeting(
        LocalDate starttime,        String location,        LocalDate endtime    ) {
        super(
        );
        this.starttime = starttime;
        this.location = location;
        this.endtime = endtime;
    }


    public LocalDate getStarttime() {
        return starttime;
    }

    public void setStarttime(LocalDate starttime) {
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


}