




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tracker_Event  {

    private int eventCode;
    private boolean correction;
    private String comments;
    private String id;
    private boolean electronicallyRead;
    private LocalDate dateTime;



    public tracker_Event(
        int eventCode,        boolean correction,        String comments,        String id,        boolean electronicallyRead,        LocalDate dateTime    ) {
        this.eventCode = eventCode;
        this.correction = correction;
        this.comments = comments;
        this.id = id;
        this.electronicallyRead = electronicallyRead;
        this.dateTime = dateTime;
    }


    public int getEventcode() {
        return eventCode;
    }

    public void setEventcode(int eventCode) {
        this.eventCode = eventCode;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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


}