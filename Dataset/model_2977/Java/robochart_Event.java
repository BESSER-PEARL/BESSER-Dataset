





import java.util.List;
import java.util.ArrayList;

public class robochart_Event extends NamedElement {

    private boolean broadcast;



    public robochart_Event(
        boolean broadcast    ) {
        super(
        );
        this.broadcast = broadcast;
    }


    public boolean getBroadcast() {
        return broadcast;
    }

    public void setBroadcast(boolean broadcast) {
        this.broadcast = broadcast;
    }


}