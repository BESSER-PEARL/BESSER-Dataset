





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_URLEvent extends Event {

    private String sourceView;



    public esmodel_events_URLEvent(
        String sourceView    ) {
        super(
        );
        this.sourceView = sourceView;
    }


    public String getSourceview() {
        return sourceView;
    }

    public void setSourceview(String sourceView) {
        this.sourceView = sourceView;
    }


}