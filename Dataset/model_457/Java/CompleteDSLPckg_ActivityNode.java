





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ActivityNode extends NamedElement, RedefinableElement {






    private CompleteDSLPckg_ActivityGroup completedslpckg_activitygroup;




    private List<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes;




    private List<CompleteDSLPckg_ActivityGroup> completedslpckg_activitygroups;


    public CompleteDSLPckg_ActivityNode(
    ) {
        super(
        );
        this.completedslpckg_activitynodes = new ArrayList<>();
        this.completedslpckg_activitygroups = new ArrayList<>();
    }

    public CompleteDSLPckg_ActivityNode(
        ArrayList<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes,        ArrayList<CompleteDSLPckg_ActivityGroup> completedslpckg_activitygroups    ) {
        this.completedslpckg_activitynodes = completedslpckg_activitynodes;
        this.completedslpckg_activitygroups = completedslpckg_activitygroups;
    }


    public CompleteDSLPckg_ActivityGroup getCompletedslpckg_activitygroup() {
        return completedslpckg_activitygroup;
    }

    public void setCompletedslpckg_activitygroup(CompleteDSLPckg_ActivityGroup completedslpckg_activitygroup) {
        this.completedslpckg_activitygroup = completedslpckg_activitygroup;
    }
    public List<CompleteDSLPckg_ActivityNode> getCompletedslpckg_activitynodes() {
        return completedslpckg_activitynodes;
    }

    public void addCompletedslpckg_activitynode(Completedslpckg_activitynode completedslpckg_activitynode) {
        this.completedslpckg_activitynodes.add(completedslpckg_activitynode);
    }
    public List<CompleteDSLPckg_ActivityGroup> getCompletedslpckg_activitygroups() {
        return completedslpckg_activitygroups;
    }

    public void addCompletedslpckg_activitygroup(Completedslpckg_activitygroup completedslpckg_activitygroup) {
        this.completedslpckg_activitygroups.add(completedslpckg_activitygroup);
    }

}