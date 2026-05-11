





import java.util.List;
import java.util.ArrayList;

public class events_Event  {

    private String timestamp;
    private boolean isProcessed;
    private String type;



    public events_Event(
        String timestamp,        boolean isProcessed,        String type    ) {
        this.timestamp = timestamp;
        this.isProcessed = isProcessed;
        this.type = type;
    }


    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public boolean getIsprocessed() {
        return isProcessed;
    }

    public void setIsprocessed(boolean isProcessed) {
        this.isProcessed = isProcessed;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}