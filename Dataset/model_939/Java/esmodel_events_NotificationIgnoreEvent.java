





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_NotificationIgnoreEvent extends Event {

    private String notificationId;



    public esmodel_events_NotificationIgnoreEvent(
        String notificationId    ) {
        super(
        );
        this.notificationId = notificationId;
    }


    public String getNotificationid() {
        return notificationId;
    }

    public void setNotificationid(String notificationId) {
        this.notificationId = notificationId;
    }


}