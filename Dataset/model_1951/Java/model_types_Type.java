





import java.util.List;
import java.util.ArrayList;

public class model_types_Type extends Node {

    private String abstract;





    private List<Variable> variables;


    public model_types_Type(
        String abstract    ) {
        super(
        );
        this.abstract = abstract;
        this.variables = new ArrayList<>();
    }

    public model_types_Type(
        String abstract        ArrayList<Variable> variables    ) {
        this.abstract = abstract;
        this.variables = variables;
    }

    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }

    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}