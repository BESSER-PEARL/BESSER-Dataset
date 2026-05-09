





import java.util.List;
import java.util.ArrayList;

public class uml_Activity extends Behavior {

    private String isSingleExecution;
    private String isReadOnly;





    private List<uml_ActivityGroup> uml_activitygroups;




    private uml_ActivityEdge uml_activityedge;




    private uml_ActivityNode uml_activitynode;




    private List<uml_ActivityNode> uml_activitynodes;




    private List<uml_ActivityEdge> uml_activityedges;




    private List<uml_ActivityPartition> uml_activitypartitions;




    private List<uml_Variable> uml_variables;




    private uml_Variable uml_variable;




    private List<uml_StructuredActivityNode> uml_structuredactivitynodes;




    private uml_ActivityGroup uml_activitygroup;


    public uml_Activity(
        String isSingleExecution,        String isReadOnly    ) {
        super(
        );
        this.isSingleExecution = isSingleExecution;
        this.isReadOnly = isReadOnly;
        this.uml_activitygroups = new ArrayList<>();
        this.uml_activitynodes = new ArrayList<>();
        this.uml_activityedges = new ArrayList<>();
        this.uml_activitypartitions = new ArrayList<>();
        this.uml_variables = new ArrayList<>();
        this.uml_structuredactivitynodes = new ArrayList<>();
    }

    public uml_Activity(
        String isSingleExecution,        String isReadOnly        ArrayList<uml_ActivityGroup> uml_activitygroups,        ArrayList<uml_ActivityNode> uml_activitynodes,        ArrayList<uml_ActivityEdge> uml_activityedges,        ArrayList<uml_ActivityPartition> uml_activitypartitions,        ArrayList<uml_Variable> uml_variables,        ArrayList<uml_StructuredActivityNode> uml_structuredactivitynodes    ) {
        this.isSingleExecution = isSingleExecution;
        this.isReadOnly = isReadOnly;
        this.uml_activitygroups = uml_activitygroups;
        this.uml_activitynodes = uml_activitynodes;
        this.uml_activityedges = uml_activityedges;
        this.uml_activitypartitions = uml_activitypartitions;
        this.uml_variables = uml_variables;
        this.uml_structuredactivitynodes = uml_structuredactivitynodes;
    }

    public String getIssingleexecution() {
        return isSingleExecution;
    }

    public void setIssingleexecution(String isSingleExecution) {
        this.isSingleExecution = isSingleExecution;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }

    public List<uml_ActivityGroup> getUml_activitygroups() {
        return uml_activitygroups;
    }

    public void addUml_activitygroup(Uml_activitygroup uml_activitygroup) {
        this.uml_activitygroups.add(uml_activitygroup);
    }
    public uml_ActivityEdge getUml_activityedge() {
        return uml_activityedge;
    }

    public void setUml_activityedge(uml_ActivityEdge uml_activityedge) {
        this.uml_activityedge = uml_activityedge;
    }
    public uml_ActivityNode getUml_activitynode() {
        return uml_activitynode;
    }

    public void setUml_activitynode(uml_ActivityNode uml_activitynode) {
        this.uml_activitynode = uml_activitynode;
    }
    public List<uml_ActivityNode> getUml_activitynodes() {
        return uml_activitynodes;
    }

    public void addUml_activitynode(Uml_activitynode uml_activitynode) {
        this.uml_activitynodes.add(uml_activitynode);
    }
    public List<uml_ActivityEdge> getUml_activityedges() {
        return uml_activityedges;
    }

    public void addUml_activityedge(Uml_activityedge uml_activityedge) {
        this.uml_activityedges.add(uml_activityedge);
    }
    public List<uml_ActivityPartition> getUml_activitypartitions() {
        return uml_activitypartitions;
    }

    public void addUml_activitypartition(Uml_activitypartition uml_activitypartition) {
        this.uml_activitypartitions.add(uml_activitypartition);
    }
    public List<uml_Variable> getUml_variables() {
        return uml_variables;
    }

    public void addUml_variable(Uml_variable uml_variable) {
        this.uml_variables.add(uml_variable);
    }
    public uml_Variable getUml_variable() {
        return uml_variable;
    }

    public void setUml_variable(uml_Variable uml_variable) {
        this.uml_variable = uml_variable;
    }
    public List<uml_StructuredActivityNode> getUml_structuredactivitynodes() {
        return uml_structuredactivitynodes;
    }

    public void addUml_structuredactivitynode(Uml_structuredactivitynode uml_structuredactivitynode) {
        this.uml_structuredactivitynodes.add(uml_structuredactivitynode);
    }
    public uml_ActivityGroup getUml_activitygroup() {
        return uml_activitygroup;
    }

    public void setUml_activitygroup(uml_ActivityGroup uml_activitygroup) {
        this.uml_activitygroup = uml_activitygroup;
    }

}