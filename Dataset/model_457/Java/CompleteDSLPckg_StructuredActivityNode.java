





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_StructuredActivityNode extends Action, Namespace, ActivityGroup, ExecutableNode {

    private boolean mustIsolate;





    private CompleteDSLPckg_ActivityNode completedslpckg_activitynode;




    private List<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes;


    public CompleteDSLPckg_StructuredActivityNode(
        boolean mustIsolate    ) {
        super(
        );
        this.mustIsolate = mustIsolate;
        this.completedslpckg_activitynodes = new ArrayList<>();
    }

    public CompleteDSLPckg_StructuredActivityNode(
        boolean mustIsolate        ArrayList<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes    ) {
        this.mustIsolate = mustIsolate;
        this.completedslpckg_activitynodes = completedslpckg_activitynodes;
    }

    public boolean getMustisolate() {
        return mustIsolate;
    }

    public void setMustisolate(boolean mustIsolate) {
        this.mustIsolate = mustIsolate;
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

}