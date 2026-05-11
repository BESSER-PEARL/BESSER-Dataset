





import java.util.List;
import java.util.ArrayList;

public class workflow_VariableDeclaration extends Declaration {

    private String isConstant;
    private String type;





    private workflow_ProcedureDeclaration workflow_proceduredeclaration;


    public workflow_VariableDeclaration(
        String isConstant,        String type    ) {
        super(
        );
        this.isConstant = isConstant;
        this.type = type;
    }


    public String getIsconstant() {
        return isConstant;
    }

    public void setIsconstant(String isConstant) {
        this.isConstant = isConstant;
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