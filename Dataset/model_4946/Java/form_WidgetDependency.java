





import java.util.List;
import java.util.ArrayList;

public class form_WidgetDependency  {

    private String eventTypes;
    private boolean triggerRefreshOnModification;



    public form_WidgetDependency(
        String eventTypes,        boolean triggerRefreshOnModification    ) {
        this.eventTypes = eventTypes;
        this.triggerRefreshOnModification = triggerRefreshOnModification;
    }


    public String getEventtypes() {
        return eventTypes;
    }

    public void setEventtypes(String eventTypes) {
        this.eventTypes = eventTypes;
    }
    public boolean getTriggerrefreshonmodification() {
        return triggerRefreshOnModification;
    }

    public void setTriggerrefreshonmodification(boolean triggerRefreshOnModification) {
        this.triggerRefreshOnModification = triggerRefreshOnModification;
    }


}