





import java.util.List;
import java.util.ArrayList;

public class model_types_CompositeVisualType extends VisualType {






    private List<Variable> variables;


    public model_types_CompositeVisualType(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public model_types_CompositeVisualType(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}