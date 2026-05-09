





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_InterruptibleActivityRegion extends ActivityGroup {






    private List<CompleteDSLPckg_ActivityEdge> completedslpckg_activityedges;




    private List<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes;




    private CompleteDSLPckg_ActivityEdge completedslpckg_activityedge;




    private CompleteDSLPckg_ActivityNode completedslpckg_activitynode;


    public CompleteDSLPckg_InterruptibleActivityRegion(
    ) {
        super(
        );
        this.completedslpckg_activityedges = new ArrayList<>();
        this.completedslpckg_activitynodes = new ArrayList<>();
    }

    public CompleteDSLPckg_InterruptibleActivityRegion(
        ArrayList<CompleteDSLPckg_ActivityEdge> completedslpckg_activityedges,        ArrayList<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes    ) {
        this.completedslpckg_activityedges = completedslpckg_activityedges;
        this.completedslpckg_activitynodes = completedslpckg_activitynodes;
    }


    public List<CompleteDSLPckg_ActivityEdge> getCompletedslpckg_activityedges() {
        return completedslpckg_activityedges;
    }

    public void addCompletedslpckg_activityedge(Completedslpckg_activityedge completedslpckg_activityedge) {
        this.completedslpckg_activityedges.add(completedslpckg_activityedge);
    }
    public List<CompleteDSLPckg_ActivityNode> getCompletedslpckg_activitynodes() {
        return completedslpckg_activitynodes;
    }

    public void addCompletedslpckg_activitynode(Completedslpckg_activitynode completedslpckg_activitynode) {
        this.completedslpckg_activitynodes.add(completedslpckg_activitynode);
    }
    public CompleteDSLPckg_ActivityEdge getCompletedslpckg_activityedge() {
        return completedslpckg_activityedge;
    }

    public void setCompletedslpckg_activityedge(CompleteDSLPckg_ActivityEdge completedslpckg_activityedge) {
        this.completedslpckg_activityedge = completedslpckg_activityedge;
    }
    public CompleteDSLPckg_ActivityNode getCompletedslpckg_activitynode() {
        return completedslpckg_activitynode;
    }

    public void setCompletedslpckg_activitynode(CompleteDSLPckg_ActivityNode completedslpckg_activitynode) {
        this.completedslpckg_activitynode = completedslpckg_activitynode;
    }

}