





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_MergeChoiceEvent extends Event {

    private String createdIssueName;
    private String selection;
    private String contextFeature;



    public esmodel_events_MergeChoiceEvent(
        String createdIssueName,        String selection,        String contextFeature    ) {
        super(
        );
        this.createdIssueName = createdIssueName;
        this.selection = selection;
        this.contextFeature = contextFeature;
    }


    public String getCreatedissuename() {
        return createdIssueName;
    }

    public void setCreatedissuename(String createdIssueName) {
        this.createdIssueName = createdIssueName;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }
    public String getContextfeature() {
        return contextFeature;
    }

    public void setContextfeature(String contextFeature) {
        this.contextFeature = contextFeature;
    }


}