





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_MergeChoiceEvent extends Event {

    private String selection;
    private String contextFeature;
    private String createdIssueName;





    private ModelElementId modelelementid;


    public esmodel_events_MergeChoiceEvent(
        String selection,        String contextFeature,        String createdIssueName    ) {
        super(
        );
        this.selection = selection;
        this.contextFeature = contextFeature;
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
    public String getCreatedissuename() {
        return createdIssueName;
    }

    public void setCreatedissuename(String createdIssueName) {
        this.createdIssueName = createdIssueName;
    }

    public ModelElementId getModelelementid() {
        return modelelementid;
    }

    public void setModelelementid(ModelElementId modelelementid) {
        this.modelelementid = modelelementid;
    }

}