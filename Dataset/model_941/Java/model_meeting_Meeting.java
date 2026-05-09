




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_meeting_Meeting extends UnicaseModelElement {

    private String location;
    private LocalDate starttime;
    private LocalDate endtime;



    public model_meeting_Meeting(
        String location,        LocalDate starttime,        LocalDate endtime    ) {
        super(
        );
        this.location = location;
        this.starttime = starttime;
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
    public LocalDate getEndtime() {
        return endtime;
    }

    public void setEndtime(LocalDate endtime) {
        this.endtime = endtime;
    }


}