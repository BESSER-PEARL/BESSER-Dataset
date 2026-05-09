





import java.util.List;
import java.util.ArrayList;

public class transformr_Pattern extends Graph {






    private List<transformr_Variable> transformr_variables;


    public transformr_Pattern(
    ) {
        super(
        );
        this.transformr_variables = new ArrayList<>();
    }

    public transformr_Pattern(
        ArrayList<transformr_Variable> transformr_variables    ) {
        this.transformr_variables = transformr_variables;
    }


    public List<transformr_Variable> getTransformr_variables() {
        return transformr_variables;
    }

    public void addTransformr_variable(Transformr_variable transformr_variable) {
        this.transformr_variables.add(transformr_variable);
    }

}