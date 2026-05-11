





import java.util.List;
import java.util.ArrayList;

public class actions_ThrowAction extends PreGenerationAction {

    private String eventID;



    public actions_ThrowAction(
        String eventID    ) {
        super(
        );
        this.eventID = eventID;
    }


    public String getEventid() {
        return eventID;
    }

    public void setEventid(String eventID) {
        this.eventID = eventID;
    }


}