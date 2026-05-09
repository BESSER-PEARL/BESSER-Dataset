





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_ReadEvent extends Event {

    private String readView;
    private String sourceView;





    private ModelElementId modelelementid;


    public esmodel_events_ReadEvent(
        String readView,        String sourceView    ) {
        super(
        );
        this.readView = readView;
        this.sourceView = sourceView;
    }


    public String getReadview() {
        return readView;
    }

    public void setReadview(String readView) {
        this.readView = readView;
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

}