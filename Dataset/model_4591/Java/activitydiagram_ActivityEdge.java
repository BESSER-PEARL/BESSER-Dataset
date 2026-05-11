





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_ActivityEdge extends ADElement {

    private boolean guard;



    public activitydiagram_ActivityEdge(
        boolean guard    ) {
        super(
        );
        this.guard = guard;
    }


    public boolean getGuard() {
        return guard;
    }

    public void setGuard(boolean guard) {
        this.guard = guard;
    }


}