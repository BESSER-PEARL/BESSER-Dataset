





import java.util.List;
import java.util.ArrayList;

public class workflow_ProcedureCall extends Expression {

    private String name;





    private List<workflow_Expression> workflow_expressions;


    public workflow_ProcedureCall(
        String name    ) {
        super(
        );
        this.name = name;
        this.workflow_expressions = new ArrayList<>();
    }

    public workflow_ProcedureCall(
        String name        ArrayList<workflow_Expression> workflow_expressions    ) {
        this.name = name;
        this.workflow_expressions = workflow_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<workflow_Expression> getWorkflow_expressions() {
        return workflow_expressions;
    }

    public void addWorkflow_expression(Workflow_expression workflow_expression) {
        this.workflow_expressions.add(workflow_expression);
    }

}