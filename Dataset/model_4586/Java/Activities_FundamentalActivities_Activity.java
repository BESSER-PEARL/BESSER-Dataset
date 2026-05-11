





import java.util.List;
import java.util.ArrayList;

public class Activities_FundamentalActivities_Activity extends Behavior {

    private boolean isSingleExecution;
    private boolean isReadOnly;





    private List<StructuredActivityNode> structuredactivitynodes;




    private List<Variable> variables;


    public Activities_FundamentalActivities_Activity(
        boolean isSingleExecution,        boolean isReadOnly    ) {
        super(
        );
        this.isSingleExecution = isSingleExecution;
        this.isReadOnly = isReadOnly;
        this.structuredactivitynodes = new ArrayList<>();
        this.variables = new ArrayList<>();
    }

    public Activities_FundamentalActivities_Activity(
        boolean isSingleExecution,        boolean isReadOnly        ArrayList<StructuredActivityNode> structuredactivitynodes,        ArrayList<Variable> variables    ) {
        this.isSingleExecution = isSingleExecution;
        this.isReadOnly = isReadOnly;
        this.structuredactivitynodes = structuredactivitynodes;
        this.variables = variables;
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

    public List<StructuredActivityNode> getStructuredactivitynodes() {
        return structuredactivitynodes;
    }

    public void addStructuredactivitynode(Structuredactivitynode structuredactivitynode) {
        this.structuredactivitynodes.add(structuredactivitynode);
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}