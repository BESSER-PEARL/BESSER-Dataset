





import java.util.List;
import java.util.ArrayList;

public class events_Event  {

    private boolean isProcessed;
    private String timestamp;
    private String type;



    public events_Event(
        boolean isProcessed,        String timestamp,        String type    ) {
        this.isProcessed = isProcessed;
        this.timestamp = timestamp;
        this.type = type;
    }


    public boolean getIsprocessed() {
        return isProcessed;
    }

    public void setIsprocessed(boolean isProcessed) {
        this.isProcessed = isProcessed;
    }
    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}