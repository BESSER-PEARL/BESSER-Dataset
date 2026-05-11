





import java.util.List;
import java.util.ArrayList;

public class workflow_Block extends Statement {






    private workflow_ProcedureDeclaration workflow_proceduredeclaration;




    private List<workflow_Statement> workflow_statements;


    public workflow_Block(
    ) {
        super(
        );
        this.workflow_statements = new ArrayList<>();
    }

    public workflow_Block(
        ArrayList<workflow_Statement> workflow_statements    ) {
        this.workflow_statements = workflow_statements;
    }


    public workflow_ProcedureDeclaration getWorkflow_proceduredeclaration() {
        return workflow_proceduredeclaration;
    }

    public void setWorkflow_proceduredeclaration(workflow_ProcedureDeclaration workflow_proceduredeclaration) {
        this.workflow_proceduredeclaration = workflow_proceduredeclaration;
    }
    public List<workflow_Statement> getWorkflow_statements() {
        return workflow_statements;
    }

    public void addWorkflow_statement(Workflow_statement workflow_statement) {
        this.workflow_statements.add(workflow_statement);
    }

}