





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_NotificationGenerationEvent extends Event {






    private List<notification_ESNotification> notification_esnotifications;


    public esmodel_events_NotificationGenerationEvent(
    ) {
        super(
        );
        this.notification_esnotifications = new ArrayList<>();
    }

    public esmodel_events_NotificationGenerationEvent(
        ArrayList<notification_ESNotification> notification_esnotifications    ) {
        this.notification_esnotifications = notification_esnotifications;
    }


    public List<notification_ESNotification> getNotification_esnotifications() {
        return notification_esnotifications;
    }

    public void addNotification_esnotification(Notification_esnotification notification_esnotification) {
        this.notification_esnotifications.add(notification_esnotification);
    }

}