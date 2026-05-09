





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_PresentationSwitchEvent extends Event {

    private String newPresentation;
    private String readView;



    public esmodel_events_PresentationSwitchEvent(
        String newPresentation,        String readView    ) {
        super(
        );
        this.newPresentation = newPresentation;
        this.readView = readView;
    }


    public String getNewpresentation() {
        return newPresentation;
    }

    public void setNewpresentation(String newPresentation) {
        this.newPresentation = newPresentation;
    }
    public String getReadview() {
        return readView;
    }

    public void setReadview(String readView) {
        this.readView = readView;
    }


}