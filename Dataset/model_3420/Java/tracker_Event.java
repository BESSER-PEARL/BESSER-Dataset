





import java.util.List;
import java.util.ArrayList;

public class tracker_Event  {

    private int eventCode;
    private String idNumber;
    private String comments;
    private String dateTime;
    private boolean correction;
    private boolean electronicallyRead;





    private tracker_Tag tracker_tag;




    private tracker_Tag tracker_tag;


    public tracker_Event(
        int eventCode,        String idNumber,        String comments,        String dateTime,        boolean correction,        boolean electronicallyRead    ) {
        this.eventCode = eventCode;
        this.idNumber = idNumber;
        this.comments = comments;
        this.dateTime = dateTime;
        this.correction = correction;
        this.electronicallyRead = electronicallyRead;
    }


    public int getEventcode() {
        return eventCode;
    }

    public void setEventcode(int eventCode) {
        this.eventCode = eventCode;
    }
    public String getIdnumber() {
        return idNumber;
    }

    public void setIdnumber(String idNumber) {
        this.idNumber = idNumber;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getDatetime() {
        return dateTime;
    }

    public void setDatetime(String dateTime) {
        this.dateTime = dateTime;
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