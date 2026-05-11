





import java.util.List;
import java.util.ArrayList;

public class workflow_LibraryFunction extends NamedElement {

    private String function;





    private List<workflow_Input> workflow_inputs;




    private List<workflow_Output> workflow_outputs;




    private workflow_Workflow workflow_workflow;


    public workflow_LibraryFunction(
        String function    ) {
        super(
        );
        this.function = function;
        this.workflow_inputs = new ArrayList<>();
        this.workflow_outputs = new ArrayList<>();
    }

    public workflow_LibraryFunction(
        String function        ArrayList<workflow_Input> workflow_inputs,        ArrayList<workflow_Output> workflow_outputs    ) {
        this.function = function;
        this.workflow_inputs = workflow_inputs;
        this.workflow_outputs = workflow_outputs;
    }

    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public List<workflow_Input> getWorkflow_inputs() {
        return workflow_inputs;
    }

    public void addWorkflow_input(Workflow_input workflow_input) {
        this.workflow_inputs.add(workflow_input);
    }
    public List<workflow_Output> getWorkflow_outputs() {
        return workflow_outputs;
    }

    public void addWorkflow_output(Workflow_output workflow_output) {
        this.workflow_outputs.add(workflow_output);
    }
    public workflow_Workflow getWorkflow_workflow() {
        return workflow_workflow;
    }

    public void setWorkflow_workflow(workflow_Workflow workflow_workflow) {
        this.workflow_workflow = workflow_workflow;
    }

}