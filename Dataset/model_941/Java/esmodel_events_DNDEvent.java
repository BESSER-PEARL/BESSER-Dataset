





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_DNDEvent extends Event {

    private String targetView;
    private String sourceView;



    public esmodel_events_DNDEvent(
        String targetView,        String sourceView    ) {
        super(
        );
        this.targetView = targetView;
        this.sourceView = sourceView;
    }


    public String getTargetview() {
        return targetView;
    }

    public void setTargetview(String targetView) {
        this.targetView = targetView;
    }
    public String getSourceview() {
        return sourceView;
    }

    public void setSourceview(String sourceView) {
        this.sourceView = sourceView;
    }


}