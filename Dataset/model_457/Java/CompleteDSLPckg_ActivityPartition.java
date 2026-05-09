





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ActivityPartition extends ActivityGroup {






    private CompleteDSLPckg_ActivityNode completedslpckg_activitynode;




    private List<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes;




    private CompleteDSLPckg_Activity completedslpckg_activity;




    private CompleteDSLPckg_ActivityEdge completedslpckg_activityedge;




    private List<CompleteDSLPckg_ActivityEdge> completedslpckg_activityedges;




    private CompleteDSLPckg_ActivityPartition completedslpckg_activitypartition;




    private CompleteDSLPckg_ActivityPartition completedslpckg_activitypartition;




    private CompleteDSLPckg_Element completedslpckg_element;


    public CompleteDSLPckg_ActivityPartition(
    ) {
        super(
        );
        this.completedslpckg_activitynodes = new ArrayList<>();
        this.completedslpckg_activityedges = new ArrayList<>();
    }

    public CompleteDSLPckg_ActivityPartition(
        ArrayList<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes,        ArrayList<CompleteDSLPckg_ActivityEdge> completedslpckg_activityedges    ) {
        this.completedslpckg_activitynodes = completedslpckg_activitynodes;
        this.completedslpckg_activityedges = completedslpckg_activityedges;
    }


    public CompleteDSLPckg_ActivityNode getCompletedslpckg_activitynode() {
        return completedslpckg_activitynode;
    }

    public void setCompletedslpckg_activitynode(CompleteDSLPckg_ActivityNode completedslpckg_activitynode) {
        this.completedslpckg_activitynode = completedslpckg_activitynode;
    }
    public List<CompleteDSLPckg_ActivityNode> getCompletedslpckg_activitynodes() {
        return completedslpckg_activitynodes;
    }

    public void addCompletedslpckg_activitynode(Completedslpckg_activitynode completedslpckg_activitynode) {
        this.completedslpckg_activitynodes.add(completedslpckg_activitynode);
    }
    public CompleteDSLPckg_Activity getCompletedslpckg_activity() {
        return completedslpckg_activity;
    }

    public void setCompletedslpckg_activity(CompleteDSLPckg_Activity completedslpckg_activity) {
        this.completedslpckg_activity = completedslpckg_activity;
    }
    public CompleteDSLPckg_ActivityEdge getCompletedslpckg_activityedge() {
        return completedslpckg_activityedge;
    }

    public void setCompletedslpckg_activityedge(CompleteDSLPckg_ActivityEdge completedslpckg_activityedge) {
        this.completedslpckg_activityedge = completedslpckg_activityedge;
    }
    public List<CompleteDSLPckg_ActivityEdge> getCompletedslpckg_activityedges() {
        return completedslpckg_activityedges;
    }

    public void addCompletedslpckg_activityedge(Completedslpckg_activityedge completedslpckg_activityedge) {
        this.completedslpckg_activityedges.add(completedslpckg_activityedge);
    }
    public CompleteDSLPckg_ActivityPartition getCompletedslpckg_activitypartition() {
        return completedslpckg_activitypartition;
    }

    public void setCompletedslpckg_activitypartition(CompleteDSLPckg_ActivityPartition completedslpckg_activitypartition) {
        this.completedslpckg_activitypartition = completedslpckg_activitypartition;
    }
    public CompleteDSLPckg_ActivityPartition getCompletedslpckg_activitypartition() {
        return completedslpckg_activitypartition;
    }

    public void setCompletedslpckg_activitypartition(CompleteDSLPckg_ActivityPartition completedslpckg_activitypartition) {
        this.completedslpckg_activitypartition = completedslpckg_activitypartition;
    }
    public CompleteDSLPckg_Element getCompletedslpckg_element() {
        return completedslpckg_element;
    }

    public void setCompletedslpckg_element(CompleteDSLPckg_Element completedslpckg_element) {
        this.completedslpckg_element = completedslpckg_element;
    }

}