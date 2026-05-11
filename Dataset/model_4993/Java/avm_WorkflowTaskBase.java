





import java.util.List;
import java.util.ArrayList;

public class avm_WorkflowTaskBase  {

    private String Name;





    private avm_Workflow avm_workflow;


    public avm_WorkflowTaskBase(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public avm_Workflow getAvm_workflow() {
        return avm_workflow;
    }

    public void setAvm_workflow(avm_Workflow avm_workflow) {
        this.avm_workflow = avm_workflow;
    }

}