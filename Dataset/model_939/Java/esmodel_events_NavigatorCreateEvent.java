





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_NavigatorCreateEvent extends Event {

    private boolean dynamic;





    private ModelElementId modelelementid;




    private ModelElementId modelelementid;


    public esmodel_events_NavigatorCreateEvent(
        boolean dynamic    ) {
        super(
        );
        this.dynamic = dynamic;
    }


    public boolean getDynamic() {
        return dynamic;
    }

    public void setDynamic(boolean dynamic) {
        this.dynamic = dynamic;
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