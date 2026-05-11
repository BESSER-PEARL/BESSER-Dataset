





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_ActivityNode extends NamedElement {

    private boolean running;





    private List<activitydiagram_ActivityEdge> activitydiagram_activityedges;




    private activitydiagram_ActivityEdge activitydiagram_activityedge;




    private activitydiagram_Activity activitydiagram_activity;




    private List<activitydiagram_ActivityEdge> activitydiagram_activityedges;




    private activitydiagram_ActivityEdge activitydiagram_activityedge;




    private activitydiagram_Activity activitydiagram_activity;


    public activitydiagram_ActivityNode(
        boolean running    ) {
        super(
        );
        this.running = running;
        this.activitydiagram_activityedges = new ArrayList<>();
        this.activitydiagram_activityedges = new ArrayList<>();
    }

    public activitydiagram_ActivityNode(
        boolean running        ArrayList<activitydiagram_ActivityEdge> activitydiagram_activityedges,        ArrayList<activitydiagram_ActivityEdge> activitydiagram_activityedges    ) {
        this.running = running;
        this.activitydiagram_activityedges = activitydiagram_activityedges;
        this.activitydiagram_activityedges = activitydiagram_activityedges;
    }

    public boolean getRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }

    public List<activitydiagram_ActivityEdge> getActivitydiagram_activityedges() {
        return activitydiagram_activityedges;
    }

    public void addActivitydiagram_activityedge(Activitydiagram_activityedge activitydiagram_activityedge) {
        this.activitydiagram_activityedges.add(activitydiagram_activityedge);
    }
    public activitydiagram_ActivityEdge getActivitydiagram_activityedge() {
        return activitydiagram_activityedge;
    }

    public void setActivitydiagram_activityedge(activitydiagram_ActivityEdge activitydiagram_activityedge) {
        this.activitydiagram_activityedge = activitydiagram_activityedge;
    }
    public activitydiagram_Activity getActivitydiagram_activity() {
        return activitydiagram_activity;
    }

    public void setActivitydiagram_activity(activitydiagram_Activity activitydiagram_activity) {
        this.activitydiagram_activity = activitydiagram_activity;
    }
    public List<activitydiagram_ActivityEdge> getActivitydiagram_activityedges() {
        return activitydiagram_activityedges;
    }

    public void addActivitydiagram_activityedge(Activitydiagram_activityedge activitydiagram_activityedge) {
        this.activitydiagram_activityedges.add(activitydiagram_activityedge);
    }
    public activitydiagram_ActivityEdge getActivitydiagram_activityedge() {
        return activitydiagram_activityedge;
    }

    public void setActivitydiagram_activityedge(activitydiagram_ActivityEdge activitydiagram_activityedge) {
        this.activitydiagram_activityedge = activitydiagram_activityedge;
    }
    public activitydiagram_Activity getActivitydiagram_activity() {
        return activitydiagram_activity;
    }

    public void setActivitydiagram_activity(activitydiagram_Activity activitydiagram_activity) {
        this.activitydiagram_activity = activitydiagram_activity;
    }

}