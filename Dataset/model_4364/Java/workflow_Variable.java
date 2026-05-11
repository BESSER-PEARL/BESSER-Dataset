





import java.util.List;
import java.util.ArrayList;

public class workflow_Variable extends Expression {

    private String name;





    private workflow_Write workflow_write;




    private workflow_Read workflow_read;




    private workflow_VariableAssignment workflow_variableassignment;


    public workflow_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_Write getWorkflow_write() {
        return workflow_write;
    }

    public void setWorkflow_write(workflow_Write workflow_write) {
        this.workflow_write = workflow_write;
    }
    public workflow_Read getWorkflow_read() {
        return workflow_read;
    }

    public void setWorkflow_read(workflow_Read workflow_read) {
        this.workflow_read = workflow_read;
    }
    public workflow_VariableAssignment getWorkflow_variableassignment() {
        return workflow_variableassignment;
    }

    public void setWorkflow_variableassignment(workflow_VariableAssignment workflow_variableassignment) {
        this.workflow_variableassignment = workflow_variableassignment;
    }

}