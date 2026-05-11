





import java.util.List;
import java.util.ArrayList;

public class iot2_ActivityNode extends NamedElement {

    private boolean running;





    private iot2_ActivityEdge iot2_activityedge;




    private List<iot2_ActivityEdge> iot2_activityedges;




    private List<iot2_ActivityEdge> iot2_activityedges;




    private iot2_ActivityEdge iot2_activityedge;




    private iot2_Activity iot2_activity;




    private iot2_Activity iot2_activity;


    public iot2_ActivityNode(
        boolean running    ) {
        super(
        );
        this.running = running;
        this.iot2_activityedges = new ArrayList<>();
        this.iot2_activityedges = new ArrayList<>();
    }

    public iot2_ActivityNode(
        boolean running        ArrayList<iot2_ActivityEdge> iot2_activityedges,        ArrayList<iot2_ActivityEdge> iot2_activityedges    ) {
        this.running = running;
        this.iot2_activityedges = iot2_activityedges;
        this.iot2_activityedges = iot2_activityedges;
    }

    public boolean getRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }

    public iot2_ActivityEdge getIot2_activityedge() {
        return iot2_activityedge;
    }

    public void setIot2_activityedge(iot2_ActivityEdge iot2_activityedge) {
        this.iot2_activityedge = iot2_activityedge;
    }
    public List<iot2_ActivityEdge> getIot2_activityedges() {
        return iot2_activityedges;
    }

    public void addIot2_activityedge(Iot2_activityedge iot2_activityedge) {
        this.iot2_activityedges.add(iot2_activityedge);
    }
    public List<iot2_ActivityEdge> getIot2_activityedges() {
        return iot2_activityedges;
    }

    public void addIot2_activityedge(Iot2_activityedge iot2_activityedge) {
        this.iot2_activityedges.add(iot2_activityedge);
    }
    public iot2_ActivityEdge getIot2_activityedge() {
        return iot2_activityedge;
    }

    public void setIot2_activityedge(iot2_ActivityEdge iot2_activityedge) {
        this.iot2_activityedge = iot2_activityedge;
    }
    public iot2_Activity getIot2_activity() {
        return iot2_activity;
    }

    public void setIot2_activity(iot2_Activity iot2_activity) {
        this.iot2_activity = iot2_activity;
    }
    public iot2_Activity getIot2_activity() {
        return iot2_activity;
    }

    public void setIot2_activity(iot2_Activity iot2_activity) {
        this.iot2_activity = iot2_activity;
    }

}