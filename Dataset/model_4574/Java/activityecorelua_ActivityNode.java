





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_ActivityNode extends NamedElement {

    private boolean running;





    private activityecorelua_Activity activityecorelua_activity;




    private activityecorelua_ActivityEdge activityecorelua_activityedge;




    private List<activityecorelua_ActivityEdge> activityecorelua_activityedges;




    private activityecorelua_Activity activityecorelua_activity;




    private List<activityecorelua_ActivityEdge> activityecorelua_activityedges;




    private activityecorelua_ActivityEdge activityecorelua_activityedge;


    public activityecorelua_ActivityNode(
        boolean running    ) {
        super(
        );
        this.running = running;
        this.activityecorelua_activityedges = new ArrayList<>();
        this.activityecorelua_activityedges = new ArrayList<>();
    }

    public activityecorelua_ActivityNode(
        boolean running        ArrayList<activityecorelua_ActivityEdge> activityecorelua_activityedges,        ArrayList<activityecorelua_ActivityEdge> activityecorelua_activityedges    ) {
        this.running = running;
        this.activityecorelua_activityedges = activityecorelua_activityedges;
        this.activityecorelua_activityedges = activityecorelua_activityedges;
    }

    public boolean getRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }

    public activityecorelua_Activity getActivityecorelua_activity() {
        return activityecorelua_activity;
    }

    public void setActivityecorelua_activity(activityecorelua_Activity activityecorelua_activity) {
        this.activityecorelua_activity = activityecorelua_activity;
    }
    public activityecorelua_ActivityEdge getActivityecorelua_activityedge() {
        return activityecorelua_activityedge;
    }

    public void setActivityecorelua_activityedge(activityecorelua_ActivityEdge activityecorelua_activityedge) {
        this.activityecorelua_activityedge = activityecorelua_activityedge;
    }
    public List<activityecorelua_ActivityEdge> getActivityecorelua_activityedges() {
        return activityecorelua_activityedges;
    }

    public void addActivityecorelua_activityedge(Activityecorelua_activityedge activityecorelua_activityedge) {
        this.activityecorelua_activityedges.add(activityecorelua_activityedge);
    }
    public activityecorelua_Activity getActivityecorelua_activity() {
        return activityecorelua_activity;
    }

    public void setActivityecorelua_activity(activityecorelua_Activity activityecorelua_activity) {
        this.activityecorelua_activity = activityecorelua_activity;
    }
    public List<activityecorelua_ActivityEdge> getActivityecorelua_activityedges() {
        return activityecorelua_activityedges;
    }

    public void addActivityecorelua_activityedge(Activityecorelua_activityedge activityecorelua_activityedge) {
        this.activityecorelua_activityedges.add(activityecorelua_activityedge);
    }
    public activityecorelua_ActivityEdge getActivityecorelua_activityedge() {
        return activityecorelua_activityedge;
    }

    public void setActivityecorelua_activityedge(activityecorelua_ActivityEdge activityecorelua_activityedge) {
        this.activityecorelua_activityedge = activityecorelua_activityedge;
    }

}