





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_PresentationSwitchEvent extends Event {

    private String readView;
    private String newPresentation;



    public esmodel_events_PresentationSwitchEvent(
        String readView,        String newPresentation    ) {
        super(
        );
        this.readView = readView;
        this.newPresentation = newPresentation;
    }


    public String getReadview() {
        return readView;
    }

    public void setReadview(String readView) {
        this.readView = readView;
    }
    public String getNewpresentation() {
        return newPresentation;
    }

    public void setNewpresentation(String newPresentation) {
        this.newPresentation = newPresentation;
    }


}