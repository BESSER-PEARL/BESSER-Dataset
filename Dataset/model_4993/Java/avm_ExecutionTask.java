





import java.util.List;
import java.util.ArrayList;

public class avm_ExecutionTask extends WorkflowTaskBase {

    private String Invocation;
    private String Description;



    public avm_ExecutionTask(
        String Invocation,        String Description    ) {
        super(
        );
        this.Invocation = Invocation;
        this.Description = Description;
    }


    public String getInvocation() {
        return Invocation;
    }

    public void setInvocation(String Invocation) {
        this.Invocation = Invocation;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }


}