





import java.util.List;
import java.util.ArrayList;

public class workflow_Operator extends Expression {






    private List<workflow_Expression> workflow_expressions;


    public workflow_Operator(
    ) {
        super(
        );
        this.workflow_expressions = new ArrayList<>();
    }

    public workflow_Operator(
        ArrayList<workflow_Expression> workflow_expressions    ) {
        this.workflow_expressions = workflow_expressions;
    }


    public List<workflow_Expression> getWorkflow_expressions() {
        return workflow_expressions;
    }

    public void addWorkflow_expression(Workflow_expression workflow_expression) {
        this.workflow_expressions.add(workflow_expression);
    }

}