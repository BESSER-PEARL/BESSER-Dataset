




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tracker_Event  {

    private boolean correction;
    private boolean electronicallyRead;
    private LocalDate dateTime;
    private String id;
    private int eventCode;
    private String comments;





    private tracker_Tag tracker_tag;




    private tracker_Tag tracker_tag;


    public tracker_Event(
        boolean correction,        boolean electronicallyRead,        LocalDate dateTime,        String id,        int eventCode,        String comments    ) {
        this.correction = correction;
        this.electronicallyRead = electronicallyRead;
        this.dateTime = dateTime;
        this.id = id;
        this.eventCode = eventCode;
        this.comments = comments;
    }


    public boolean getCorrection() {
        return correction;
    }

    public void setCorrection(boolean correction) {
        this.correction = correction;
    }
    public boolean getElectronicallyread() {
        return electronicallyRead;
    }

    public void setElectronicallyread(boolean electronicallyRead) {
        this.electronicallyRead = electronicallyRead;
    }
    public LocalDate getDatetime() {
        return dateTime;
    }

    public void setDatetime(LocalDate dateTime) {
        this.dateTime = dateTime;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getEventcode() {
        return eventCode;
    }

    public void setEventcode(int eventCode) {
        this.eventCode = eventCode;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public tracker_Tag getTracker_tag() {
        return tracker_tag;
    }

    public void setTracker_tag(tracker_Tag tracker_tag) {
        this.tracker_tag = tracker_tag;
    }
    public tracker_Tag getTracker_tag() {
        return tracker_tag;
    }

    public void setTracker_tag(tracker_Tag tracker_tag) {
        this.tracker_tag = tracker_tag;
    }

}