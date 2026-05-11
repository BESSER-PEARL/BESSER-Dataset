





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_JoinNode extends ControlNode {






    private List<activitydiagram_ActivityEdge> activitydiagram_activityedges;




    private activitydiagram_ActivityEdge activitydiagram_activityedge;


    public activitydiagram_JoinNode(
    ) {
        super(
        );
        this.activitydiagram_activityedges = new ArrayList<>();
    }

    public activitydiagram_JoinNode(
        ArrayList<activitydiagram_ActivityEdge> activitydiagram_activityedges    ) {
        this.activitydiagram_activityedges = activitydiagram_activityedges;
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