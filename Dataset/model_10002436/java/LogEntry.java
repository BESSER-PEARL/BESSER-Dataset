





import java.util.List;
import java.util.ArrayList;

public class LogEntry  {

    private String time;
    private String objectType;
    private String objectId;
    private String _attr;



    public LogEntry(
        String time,        String objectType,        String objectId,        String _attr    ) {
        this.time = time;
        this.objectType = objectType;
        this.objectId = objectId;
        this._attr = _attr;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getObjecttype() {
        return objectType;
    }

    public void setObjecttype(String objectType) {
        this.objectType = objectType;
    }
    public String getObjectid() {
        return objectId;
    }

    public void setObjectid(String objectId) {
        this.objectId = objectId;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }


}