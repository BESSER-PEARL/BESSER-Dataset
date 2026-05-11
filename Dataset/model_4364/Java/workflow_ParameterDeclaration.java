





import java.util.List;
import java.util.ArrayList;

public class workflow_ParameterDeclaration extends Declaration {

    private String type;





    private workflow_ProcedureDeclaration workflow_proceduredeclaration;


    public workflow_ParameterDeclaration(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public workflow_ProcedureDeclaration getWorkflow_proceduredeclaration() {
        return workflow_proceduredeclaration;
    }

    public void setWorkflow_proceduredeclaration(workflow_ProcedureDeclaration workflow_proceduredeclaration) {
        this.workflow_proceduredeclaration = workflow_proceduredeclaration;
    }

}