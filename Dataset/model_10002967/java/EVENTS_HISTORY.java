





import java.util.List;
import java.util.ArrayList;

public class EVENTS_HISTORY  {

    private String createdAt;
    private String newValue;
    private String _id;
    private String eventId;
    private String userId;
    private String oldValue;



    public EVENTS_HISTORY(
        String createdAt,        String newValue,        String _id,        String eventId,        String userId,        String oldValue    ) {
        this.createdAt = createdAt;
        this.newValue = newValue;
        this._id = _id;
        this.eventId = eventId;
        this.userId = userId;
        this.oldValue = oldValue;
    }


    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String getNewvalue() {
        return newValue;
    }

    public void setNewvalue(String newValue) {
        this.newValue = newValue;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getEventid() {
        return eventId;
    }

    public void setEventid(String eventId) {
        this.eventId = eventId;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getOldvalue() {
        return oldValue;
    }

    public void setOldvalue(String oldValue) {
        this.oldValue = oldValue;
    }


}