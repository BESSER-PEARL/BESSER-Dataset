





import java.util.List;
import java.util.ArrayList;

public class avm_ExecutionTask extends WorkflowTaskBase {

    private String Description;
    private String Invocation;



    public avm_ExecutionTask(
        String Description,        String Invocation    ) {
        super(
        );
        this.Description = Description;
        this.Invocation = Invocation;
    }


    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getInvocation() {
        return Invocation;
    }

    public void setInvocation(String Invocation) {
        this.Invocation = Invocation;
    }


}