





import java.util.List;
import java.util.ArrayList;

public class xmof_CompleteStructuredActivities_ConditionalNode extends StructuredActivityNode {

    private boolean assured;
    private boolean determinate;





    private List<CompleteStructuredActivities_Clause> completestructuredactivities_clauses;


    public xmof_CompleteStructuredActivities_ConditionalNode(
        boolean assured,        boolean determinate    ) {
        super(
        );
        this.assured = assured;
        this.determinate = determinate;
        this.completestructuredactivities_clauses = new ArrayList<>();
    }

    public xmof_CompleteStructuredActivities_ConditionalNode(
        boolean assured,        boolean determinate        ArrayList<CompleteStructuredActivities_Clause> completestructuredactivities_clauses    ) {
        this.assured = assured;
        this.determinate = determinate;
        this.completestructuredactivities_clauses = completestructuredactivities_clauses;
    }

    public boolean getAssured() {
        return assured;
    }

    public void setAssured(boolean assured) {
        this.assured = assured;
    }
    public boolean getDeterminate() {
        return determinate;
    }

    public void setDeterminate(boolean determinate) {
        this.determinate = determinate;
    }

    public List<CompleteStructuredActivities_Clause> getCompletestructuredactivities_clauses() {
        return completestructuredactivities_clauses;
    }

    public void addCompletestructuredactivities_clause(Completestructuredactivities_clause completestructuredactivities_clause) {
        this.completestructuredactivities_clauses.add(completestructuredactivities_clause);
    }

}