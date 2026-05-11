





import java.util.List;
import java.util.ArrayList;

public class workflow_Condition extends Statement {

    private String expression;
    private String description;





    private workflow_Statement workflow_statement;




    private workflow_Statement workflow_statement;


    public workflow_Condition(
        String expression,        String description    ) {
        super(
        );
        this.expression = expression;
        this.description = description;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public workflow_Statement getWorkflow_statement() {
        return workflow_statement;
    }

    public void setWorkflow_statement(workflow_Statement workflow_statement) {
        this.workflow_statement = workflow_statement;
    }
    public workflow_Statement getWorkflow_statement() {
        return workflow_statement;
    }

    public void setWorkflow_statement(workflow_Statement workflow_statement) {
        this.workflow_statement = workflow_statement;
    }

}