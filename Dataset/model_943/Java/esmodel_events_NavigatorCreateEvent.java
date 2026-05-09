





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_NavigatorCreateEvent extends Event {

    private boolean dynamic;



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


}