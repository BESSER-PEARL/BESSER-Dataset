





import java.util.List;
import java.util.ArrayList;

public class fUML_CompleteStructuredActivities_ConditionalNode extends StructuredActivityNode {

    private boolean determinate;
    private boolean assured;





    private List<CompleteStructuredActivities_Clause> completestructuredactivities_clauses;


    public fUML_CompleteStructuredActivities_ConditionalNode(
        boolean determinate,        boolean assured    ) {
        super(
        );
        this.determinate = determinate;
        this.assured = assured;
        this.completestructuredactivities_clauses = new ArrayList<>();
    }

    public fUML_CompleteStructuredActivities_ConditionalNode(
        boolean determinate,        boolean assured        ArrayList<CompleteStructuredActivities_Clause> completestructuredactivities_clauses    ) {
        this.determinate = determinate;
        this.assured = assured;
        this.completestructuredactivities_clauses = completestructuredactivities_clauses;
    }

    public boolean getDeterminate() {
        return determinate;
    }

    public void setDeterminate(boolean determinate) {
        this.determinate = determinate;
    }
    public boolean getAssured() {
        return assured;
    }

    public void setAssured(boolean assured) {
        this.assured = assured;
    }

    public List<CompleteStructuredActivities_Clause> getCompletestructuredactivities_clauses() {
        return completestructuredactivities_clauses;
    }

    public void addCompletestructuredactivities_clause(Completestructuredactivities_clause completestructuredactivities_clause) {
        this.completestructuredactivities_clauses.add(completestructuredactivities_clause);
    }

}