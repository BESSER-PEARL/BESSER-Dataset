





import java.util.List;
import java.util.ArrayList;

public class tracker_Event  {

    private String id;
    private String dateTime;
    private boolean correction;
    private String comments;
    private int eventCode;
    private boolean electronicallyRead;





    private tracker_AnimalId tracker_animalid;


    public tracker_Event(
        String id,        String dateTime,        boolean correction,        String comments,        int eventCode,        boolean electronicallyRead    ) {
        this.id = id;
        this.dateTime = dateTime;
        this.correction = correction;
        this.comments = comments;
        this.eventCode = eventCode;
        this.electronicallyRead = electronicallyRead;
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
    public boolean getCorrection() {
        return correction;
    }

    public void setCorrection(boolean correction) {
        this.correction = correction;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public int getEventcode() {
        return eventCode;
    }

    public void setEventcode(int eventCode) {
        this.eventCode = eventCode;
    }
    public boolean getElectronicallyread() {
        return electronicallyRead;
    }

    public void setElectronicallyread(boolean electronicallyRead) {
        this.electronicallyRead = electronicallyRead;
    }

    public tracker_AnimalId getTracker_animalid() {
        return tracker_animalid;
    }

    public void setTracker_animalid(tracker_AnimalId tracker_animalid) {
        this.tracker_animalid = tracker_animalid;
    }

}