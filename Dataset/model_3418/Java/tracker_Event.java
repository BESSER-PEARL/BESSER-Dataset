





import java.util.List;
import java.util.ArrayList;

public class tracker_Event  {

    private boolean correction;
    private boolean electronicallyRead;
    private String idNumber;
    private String comments;
    private String id;
    private String dateTime;
    private int eventCode;





    private tracker_Tag tracker_tag;




    private tracker_Tag tracker_tag;


    public tracker_Event(
        boolean correction,        boolean electronicallyRead,        String idNumber,        String comments,        String id,        String dateTime,        int eventCode    ) {
        this.correction = correction;
        this.electronicallyRead = electronicallyRead;
        this.idNumber = idNumber;
        this.comments = comments;
        this.id = id;
        this.dateTime = dateTime;
        this.eventCode = eventCode;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDatetime() {
        return dateTime;
    }

    public void setDatetime(String dateTime) {
        this.dateTime = dateTime;
    }
    public int getEventcode() {
        return eventCode;
    }

    public void setEventcode(int eventCode) {
        this.eventCode = eventCode;
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