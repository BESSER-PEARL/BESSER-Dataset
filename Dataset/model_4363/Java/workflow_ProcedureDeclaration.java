





import java.util.List;
import java.util.ArrayList;

public class workflow_ProcedureDeclaration extends Declaration {

    private String returnType;
    private String accessModifier;





    private workflow_CompilationUnit workflow_compilationunit;


    public workflow_ProcedureDeclaration(
        String returnType,        String accessModifier    ) {
        super(
        );
        this.returnType = returnType;
        this.accessModifier = accessModifier;
    }


    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getAccessmodifier() {
        return accessModifier;
    }

    public void setAccessmodifier(String accessModifier) {
        this.accessModifier = accessModifier;
    }

    public workflow_CompilationUnit getWorkflow_compilationunit() {
        return workflow_compilationunit;
    }

    public void setWorkflow_compilationunit(workflow_CompilationUnit workflow_compilationunit) {
        this.workflow_compilationunit = workflow_compilationunit;
    }

}