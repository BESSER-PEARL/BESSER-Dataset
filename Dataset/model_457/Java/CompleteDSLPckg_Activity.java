





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Activity extends Behavior {

    private boolean isSingleExecution;
    private boolean isReadOnly;





    private List<CompleteDSLPckg_ActivityGroup> completedslpckg_activitygroups;




    private List<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes;




    private List<CompleteDSLPckg_Variable> completedslpckg_variables;




    private List<CompleteDSLPckg_ActivityEdge> completedslpckg_activityedges;




    private List<CompleteDSLPckg_StructuredActivityNode> completedslpckg_structuredactivitynodes;




    private CompleteDSLPckg_StructuredActivityNode completedslpckg_structuredactivitynode;




    private CompleteDSLPckg_ActivityGroup completedslpckg_activitygroup;


    public CompleteDSLPckg_Activity(
        boolean isSingleExecution,        boolean isReadOnly    ) {
        super(
        );
        this.isSingleExecution = isSingleExecution;
        this.isReadOnly = isReadOnly;
        this.completedslpckg_activitygroups = new ArrayList<>();
        this.completedslpckg_activitynodes = new ArrayList<>();
        this.completedslpckg_variables = new ArrayList<>();
        this.completedslpckg_activityedges = new ArrayList<>();
        this.completedslpckg_structuredactivitynodes = new ArrayList<>();
    }

    public CompleteDSLPckg_Activity(
        boolean isSingleExecution,        boolean isReadOnly        ArrayList<CompleteDSLPckg_ActivityGroup> completedslpckg_activitygroups,        ArrayList<CompleteDSLPckg_ActivityNode> completedslpckg_activitynodes,        ArrayList<CompleteDSLPckg_Variable> completedslpckg_variables,        ArrayList<CompleteDSLPckg_ActivityEdge> completedslpckg_activityedges,        ArrayList<CompleteDSLPckg_StructuredActivityNode> completedslpckg_structuredactivitynodes    ) {
        this.isSingleExecution = isSingleExecution;
        this.isReadOnly = isReadOnly;
        this.completedslpckg_activitygroups = completedslpckg_activitygroups;
        this.completedslpckg_activitynodes = completedslpckg_activitynodes;
        this.completedslpckg_variables = completedslpckg_variables;
        this.completedslpckg_activityedges = completedslpckg_activityedges;
        this.completedslpckg_structuredactivitynodes = completedslpckg_structuredactivitynodes;
    }

    public boolean getIssingleexecution() {
        return isSingleExecution;
    }

    public void setIssingleexecution(boolean isSingleExecution) {
        this.isSingleExecution = isSingleExecution;
    }
    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }

    public List<CompleteDSLPckg_ActivityGroup> getCompletedslpckg_activitygroups() {
        return completedslpckg_activitygroups;
    }

    public void addCompletedslpckg_activitygroup(Completedslpckg_activitygroup completedslpckg_activitygroup) {
        this.completedslpckg_activitygroups.add(completedslpckg_activitygroup);
    }
    public List<CompleteDSLPckg_ActivityNode> getCompletedslpckg_activitynodes() {
        return completedslpckg_activitynodes;
    }

    public void addCompletedslpckg_activitynode(Completedslpckg_activitynode completedslpckg_activitynode) {
        this.completedslpckg_activitynodes.add(completedslpckg_activitynode);
    }
    public List<CompleteDSLPckg_Variable> getCompletedslpckg_variables() {
        return completedslpckg_variables;
    }

    public void addCompletedslpckg_variable(Completedslpckg_variable completedslpckg_variable) {
        this.completedslpckg_variables.add(completedslpckg_variable);
    }
    public List<CompleteDSLPckg_ActivityEdge> getCompletedslpckg_activityedges() {
        return completedslpckg_activityedges;
    }

    public void addCompletedslpckg_activityedge(Completedslpckg_activityedge completedslpckg_activityedge) {
        this.completedslpckg_activityedges.add(completedslpckg_activityedge);
    }
    public List<CompleteDSLPckg_StructuredActivityNode> getCompletedslpckg_structuredactivitynodes() {
        return completedslpckg_structuredactivitynodes;
    }

    public void addCompletedslpckg_structuredactivitynode(Completedslpckg_structuredactivitynode completedslpckg_structuredactivitynode) {
        this.completedslpckg_structuredactivitynodes.add(completedslpckg_structuredactivitynode);
    }
    public CompleteDSLPckg_StructuredActivityNode getCompletedslpckg_structuredactivitynode() {
        return completedslpckg_structuredactivitynode;
    }

    public void setCompletedslpckg_structuredactivitynode(CompleteDSLPckg_StructuredActivityNode completedslpckg_structuredactivitynode) {
        this.completedslpckg_structuredactivitynode = completedslpckg_structuredactivitynode;
    }
    public CompleteDSLPckg_ActivityGroup getCompletedslpckg_activitygroup() {
        return completedslpckg_activitygroup;
    }

    public void setCompletedslpckg_activitygroup(CompleteDSLPckg_ActivityGroup completedslpckg_activitygroup) {
        this.completedslpckg_activitygroup = completedslpckg_activitygroup;
    }

}