





import java.util.List;
import java.util.ArrayList;

public class commons_EventBusProgressMonitor extends ProgressMonitor {

    private String eventBus;
    private String trackingId;



    public commons_EventBusProgressMonitor(
        String eventBus,        String trackingId    ) {
        super(
        );
        this.eventBus = eventBus;
        this.trackingId = trackingId;
    }


    public String getEventbus() {
        return eventBus;
    }

    public void setEventbus(String eventBus) {
        this.eventBus = eventBus;
    }
    public String getTrackingid() {
        return trackingId;
    }

    public void setTrackingid(String trackingId) {
        this.trackingId = trackingId;
    }


}