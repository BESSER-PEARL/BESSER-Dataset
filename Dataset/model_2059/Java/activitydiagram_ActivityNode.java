





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_ActivityNode extends NamedElement {

    private boolean running;



    public activitydiagram_ActivityNode(
        boolean running    ) {
        super(
        );
        this.running = running;
    }


    public boolean getRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }


}