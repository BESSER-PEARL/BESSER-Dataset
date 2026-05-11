





import java.util.List;
import java.util.ArrayList;

public class workflow_Expression extends Statement {






    private workflow_VariableAssignment workflow_variableassignment;




    private workflow_ProcedureReturn workflow_procedurereturn;




    private workflow_If workflow_if;




    private workflow_While workflow_while;


    public workflow_Expression(
    ) {
        super(
        );
    }



    public workflow_VariableAssignment getWorkflow_variableassignment() {
        return workflow_variableassignment;
    }

    public void setWorkflow_variableassignment(workflow_VariableAssignment workflow_variableassignment) {
        this.workflow_variableassignment = workflow_variableassignment;
    }
    public workflow_ProcedureReturn getWorkflow_procedurereturn() {
        return workflow_procedurereturn;
    }

    public void setWorkflow_procedurereturn(workflow_ProcedureReturn workflow_procedurereturn) {
        this.workflow_procedurereturn = workflow_procedurereturn;
    }
    public workflow_If getWorkflow_if() {
        return workflow_if;
    }

    public void setWorkflow_if(workflow_If workflow_if) {
        this.workflow_if = workflow_if;
    }
    public workflow_While getWorkflow_while() {
        return workflow_while;
    }

    public void setWorkflow_while(workflow_While workflow_while) {
        this.workflow_while = workflow_while;
    }

}