





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_DNDEvent extends Event {

    private String sourceView;
    private String targetView;





    private ModelElementId modelelementid;




    private ModelElementId modelelementid;


    public esmodel_events_DNDEvent(
        String sourceView,        String targetView    ) {
        super(
        );
        this.sourceView = sourceView;
        this.targetView = targetView;
    }


    public String getSourceview() {
        return sourceView;
    }

    public void setSourceview(String sourceView) {
        this.sourceView = sourceView;
    }
    public String getTargetview() {
        return targetView;
    }

    public void setTargetview(String targetView) {
        this.targetView = targetView;
    }

    public ModelElementId getModelelementid() {
        return modelelementid;
    }

    public void setModelelementid(ModelElementId modelelementid) {
        this.modelelementid = modelelementid;
    }
    public ModelElementId getModelelementid() {
        return modelelementid;
    }

    public void setModelelementid(ModelElementId modelelementid) {
        this.modelelementid = modelelementid;
    }

}