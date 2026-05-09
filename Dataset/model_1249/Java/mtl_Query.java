





import java.util.List;
import java.util.ArrayList;

public class mtl_Query extends ModuleElement, DocumentedElement {






    private mtl_QueryInvocation mtl_queryinvocation;




    private List<Variable> variables;


    public mtl_Query(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public mtl_Query(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public mtl_QueryInvocation getMtl_queryinvocation() {
        return mtl_queryinvocation;
    }

    public void setMtl_queryinvocation(mtl_QueryInvocation mtl_queryinvocation) {
        this.mtl_queryinvocation = mtl_queryinvocation;
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}