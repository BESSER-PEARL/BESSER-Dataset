





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_ActivityNode extends ADElement {

    private boolean current;





    private List<activitydiagram_ActivityEdge> activitydiagram_activityedges;




    private activitydiagram_ActivityEdge activitydiagram_activityedge;




    private List<activitydiagram_ActivityEdge> activitydiagram_activityedges;




    private activitydiagram_ActivityEdge activitydiagram_activityedge;


    public activitydiagram_ActivityNode(
        boolean current    ) {
        super(
        );
        this.current = current;
        this.activitydiagram_activityedges = new ArrayList<>();
        this.activitydiagram_activityedges = new ArrayList<>();
    }

    public activitydiagram_ActivityNode(
        boolean current        ArrayList<activitydiagram_ActivityEdge> activitydiagram_activityedges,        ArrayList<activitydiagram_ActivityEdge> activitydiagram_activityedges    ) {
        this.current = current;
        this.activitydiagram_activityedges = activitydiagram_activityedges;
        this.activitydiagram_activityedges = activitydiagram_activityedges;
    }

    public boolean getCurrent() {
        return current;
    }

    public void setCurrent(boolean current) {
        this.current = current;
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

}