





import java.util.List;
import java.util.ArrayList;

public class workflow_ForEach extends Statement {

    private String element;
    private String sequence;





    private List<workflow_Statement> workflow_statements;


    public workflow_ForEach(
        String element,        String sequence    ) {
        super(
        );
        this.element = element;
        this.sequence = sequence;
        this.workflow_statements = new ArrayList<>();
    }

    public workflow_ForEach(
        String element,        String sequence        ArrayList<workflow_Statement> workflow_statements    ) {
        this.element = element;
        this.sequence = sequence;
        this.workflow_statements = workflow_statements;
    }

    public String getElement() {
        return element;
    }

    public void setElement(String element) {
        this.element = element;
    }
    public String getSequence() {
        return sequence;
    }

    public void setSequence(String sequence) {
        this.sequence = sequence;
    }

    public List<workflow_Statement> getWorkflow_statements() {
        return workflow_statements;
    }

    public void addWorkflow_statement(Workflow_statement workflow_statement) {
        this.workflow_statements.add(workflow_statement);
    }

}