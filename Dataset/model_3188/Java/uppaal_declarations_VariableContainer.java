





import java.util.List;
import java.util.ArrayList;

public class uppaal_declarations_VariableContainer  {






    private TypeDefinition typedefinition;




    private List<Variable> variables;


    public uppaal_declarations_VariableContainer(
    ) {
        this.variables = new ArrayList<>();
    }

    public uppaal_declarations_VariableContainer(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public TypeDefinition getTypedefinition() {
        return typedefinition;
    }

    public void setTypedefinition(TypeDefinition typedefinition) {
        this.typedefinition = typedefinition;
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}