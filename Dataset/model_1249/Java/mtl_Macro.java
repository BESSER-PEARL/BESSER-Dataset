





import java.util.List;
import java.util.ArrayList;

public class mtl_Macro extends ModuleElement, Block, DocumentedElement {






    private mtl_MacroInvocation mtl_macroinvocation;




    private mtl_EClassifier mtl_eclassifier;




    private List<Variable> variables;


    public mtl_Macro(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public mtl_Macro(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public mtl_MacroInvocation getMtl_macroinvocation() {
        return mtl_macroinvocation;
    }

    public void setMtl_macroinvocation(mtl_MacroInvocation mtl_macroinvocation) {
        this.mtl_macroinvocation = mtl_macroinvocation;
    }
    public mtl_EClassifier getMtl_eclassifier() {
        return mtl_eclassifier;
    }

    public void setMtl_eclassifier(mtl_EClassifier mtl_eclassifier) {
        this.mtl_eclassifier = mtl_eclassifier;
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}