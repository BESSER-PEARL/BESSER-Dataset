





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_ReadEvent extends Event {

    private String sourceView;
    private String readView;



    public esmodel_events_ReadEvent(
        String sourceView,        String readView    ) {
        super(
        );
        this.sourceView = sourceView;
        this.readView = readView;
    }


    public String getSourceview() {
        return sourceView;
    }

    public void setSourceview(String sourceView) {
        this.sourceView = sourceView;
    }
    public String getReadview() {
        return readView;
    }

    public void setReadview(String readView) {
        this.readView = readView;
    }


}