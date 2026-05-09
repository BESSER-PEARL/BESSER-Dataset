




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_meeting_Meeting extends UnicaseModelElement {

    private LocalDate endtime;
    private String location;
    private LocalDate starttime;



    public model_meeting_Meeting(
        LocalDate endtime,        String location,        LocalDate starttime    ) {
        super(
        );
        this.endtime = endtime;
        this.location = location;
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
    public LocalDate getStarttime() {
        return starttime;
    }

    public void setStarttime(LocalDate starttime) {
        this.starttime = starttime;
    }


}