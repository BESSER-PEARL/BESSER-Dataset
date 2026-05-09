





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_MergeChoiceEvent extends Event {

    private String createdIssueName;
    private String contextFeature;
    private String selection;





    private ModelElementId modelelementid;


    public esmodel_events_MergeChoiceEvent(
        String createdIssueName,        String contextFeature,        String selection    ) {
        super(
        );
        this.createdIssueName = createdIssueName;
        this.contextFeature = contextFeature;
        this.selection = selection;
    }


    public String getCreatedissuename() {
        return createdIssueName;
    }

    public void setCreatedissuename(String createdIssueName) {
        this.createdIssueName = createdIssueName;
    }
    public String getContextfeature() {
        return contextFeature;
    }

    public void setContextfeature(String contextFeature) {
        this.contextFeature = contextFeature;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }

    public ModelElementId getModelelementid() {
        return modelelementid;
    }

    public void setModelelementid(ModelElementId modelelementid) {
        this.modelelementid = modelelementid;
    }

}