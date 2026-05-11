





import java.util.List;
import java.util.ArrayList;

public class model_BasicNotificationDefinition extends BasicObject {

    private boolean active;
    private String identifier;
    private String description;
    private String notificationEventId;



    public model_BasicNotificationDefinition(
        boolean active,        String identifier,        String description,        String notificationEventId    ) {
        super(
        );
        this.active = active;
        this.identifier = identifier;
        this.description = description;
        this.notificationEventId = notificationEventId;
    }


    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getNotificationeventid() {
        return notificationEventId;
    }

    public void setNotificationeventid(String notificationEventId) {
        this.notificationEventId = notificationEventId;
    }


}