





import java.util.List;
import java.util.ArrayList;

public class EVENTS_LIST  {

    private String key;
    private String createdAt;
    private String _id;
    private String description;





    private EVENTS_HISTORY events_history;


    public EVENTS_LIST(
        String key,        String createdAt,        String _id,        String description    ) {
        this.key = key;
        this.createdAt = createdAt;
        this._id = _id;
        this.description = description;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public EVENTS_HISTORY getEvents_history() {
        return events_history;
    }

    public void setEvents_history(EVENTS_HISTORY events_history) {
        this.events_history = events_history;
    }

}