





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Activity extends Behavior {

    private String isReadOnly;
    private String isSingleExecution;
    private String structuredNode;
    private String partition;





    private List<UMLModel_Variable> umlmodel_variables;




    private List<UMLModel_ActivityEdge> umlmodel_activityedges;




    private List<UMLModel_ActivityGroup> umlmodel_activitygroups;


    public UMLModel_Activity(
        String isReadOnly,        String isSingleExecution,        String structuredNode,        String partition    ) {
        super(
        );
        this.isReadOnly = isReadOnly;
        this.isSingleExecution = isSingleExecution;
        this.structuredNode = structuredNode;
        this.partition = partition;
        this.umlmodel_variables = new ArrayList<>();
        this.umlmodel_activityedges = new ArrayList<>();
        this.umlmodel_activitygroups = new ArrayList<>();
    }

    public UMLModel_Activity(
        String isReadOnly,        String isSingleExecution,        String structuredNode,        String partition        ArrayList<UMLModel_Variable> umlmodel_variables,        ArrayList<UMLModel_ActivityEdge> umlmodel_activityedges,        ArrayList<UMLModel_ActivityGroup> umlmodel_activitygroups    ) {
        this.isReadOnly = isReadOnly;
        this.isSingleExecution = isSingleExecution;
        this.structuredNode = structuredNode;
        this.partition = partition;
        this.umlmodel_variables = umlmodel_variables;
        this.umlmodel_activityedges = umlmodel_activityedges;
        this.umlmodel_activitygroups = umlmodel_activitygroups;
    }

    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getIssingleexecution() {
        return isSingleExecution;
    }

    public void setIssingleexecution(String isSingleExecution) {
        this.isSingleExecution = isSingleExecution;
    }
    public String getStructurednode() {
        return structuredNode;
    }

    public void setStructurednode(String structuredNode) {
        this.structuredNode = structuredNode;
    }
    public String getPartition() {
        return partition;
    }

    public void setPartition(String partition) {
        this.partition = partition;
    }

    public List<UMLModel_Variable> getUmlmodel_variables() {
        return umlmodel_variables;
    }

    public void addUmlmodel_variable(Umlmodel_variable umlmodel_variable) {
        this.umlmodel_variables.add(umlmodel_variable);
    }
    public List<UMLModel_ActivityEdge> getUmlmodel_activityedges() {
        return umlmodel_activityedges;
    }

    public void addUmlmodel_activityedge(Umlmodel_activityedge umlmodel_activityedge) {
        this.umlmodel_activityedges.add(umlmodel_activityedge);
    }
    public List<UMLModel_ActivityGroup> getUmlmodel_activitygroups() {
        return umlmodel_activitygroups;
    }

    public void addUmlmodel_activitygroup(Umlmodel_activitygroup umlmodel_activitygroup) {
        this.umlmodel_activitygroups.add(umlmodel_activitygroup);
    }

}