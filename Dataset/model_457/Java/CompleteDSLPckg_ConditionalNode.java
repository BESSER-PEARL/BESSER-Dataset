





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ConditionalNode extends StructuredActivityNode {

    private boolean isAssumed;
    private boolean isDeterminate;





    private List<CompleteDSLPckg_ExecutableNode> completedslpckg_executablenodes;




    private List<CompleteDSLPckg_Clause> completedslpckg_clauses;




    private List<CompleteDSLPckg_ExecutableNode> completedslpckg_executablenodes;


    public CompleteDSLPckg_ConditionalNode(
        boolean isAssumed,        boolean isDeterminate    ) {
        super(
        );
        this.isAssumed = isAssumed;
        this.isDeterminate = isDeterminate;
        this.completedslpckg_executablenodes = new ArrayList<>();
        this.completedslpckg_clauses = new ArrayList<>();
        this.completedslpckg_executablenodes = new ArrayList<>();
    }

    public CompleteDSLPckg_ConditionalNode(
        boolean isAssumed,        boolean isDeterminate        ArrayList<CompleteDSLPckg_ExecutableNode> completedslpckg_executablenodes,        ArrayList<CompleteDSLPckg_Clause> completedslpckg_clauses,        ArrayList<CompleteDSLPckg_ExecutableNode> completedslpckg_executablenodes    ) {
        this.isAssumed = isAssumed;
        this.isDeterminate = isDeterminate;
        this.completedslpckg_executablenodes = completedslpckg_executablenodes;
        this.completedslpckg_clauses = completedslpckg_clauses;
        this.completedslpckg_executablenodes = completedslpckg_executablenodes;
    }

    public boolean getIsassumed() {
        return isAssumed;
    }

    public void setIsassumed(boolean isAssumed) {
        this.isAssumed = isAssumed;
    }
    public boolean getIsdeterminate() {
        return isDeterminate;
    }

    public void setIsdeterminate(boolean isDeterminate) {
        this.isDeterminate = isDeterminate;
    }

    public List<CompleteDSLPckg_ExecutableNode> getCompletedslpckg_executablenodes() {
        return completedslpckg_executablenodes;
    }

    public void addCompletedslpckg_executablenode(Completedslpckg_executablenode completedslpckg_executablenode) {
        this.completedslpckg_executablenodes.add(completedslpckg_executablenode);
    }
    public List<CompleteDSLPckg_Clause> getCompletedslpckg_clauses() {
        return completedslpckg_clauses;
    }

    public void addCompletedslpckg_clause(Completedslpckg_clause completedslpckg_clause) {
        this.completedslpckg_clauses.add(completedslpckg_clause);
    }
    public List<CompleteDSLPckg_ExecutableNode> getCompletedslpckg_executablenodes() {
        return completedslpckg_executablenodes;
    }

    public void addCompletedslpckg_executablenode(Completedslpckg_executablenode completedslpckg_executablenode) {
        this.completedslpckg_executablenodes.add(completedslpckg_executablenode);
    }

}