





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_NotificationReadEvent extends ReadEvent {

    private String notificationId;



    public esmodel_events_NotificationReadEvent(
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