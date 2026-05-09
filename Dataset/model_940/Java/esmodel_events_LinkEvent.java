





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_LinkEvent extends Event {

    private boolean createdNew;
    private String sourceView;





    private ModelElementId modelelementid;




    private ModelElementId modelelementid;


    public esmodel_events_LinkEvent(
        boolean createdNew,        String sourceView    ) {
        super(
        );
        this.createdNew = createdNew;
        this.sourceView = sourceView;
    }


    public boolean getCreatednew() {
        return createdNew;
    }

    public void setCreatednew(boolean createdNew) {
        this.createdNew = createdNew;
    }
    public String getSourceview() {
        return sourceView;
    }

    public void setSourceview(String sourceView) {
        this.sourceView = sourceView;
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