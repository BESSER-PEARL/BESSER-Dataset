





import java.util.List;
import java.util.ArrayList;

public class qvtrelation_Relation extends Rule {

    private String isTopLevel;





    private List<Variable> variables;


    public qvtrelation_Relation(
        String isTopLevel    ) {
        super(
        );
        this.isTopLevel = isTopLevel;
        this.variables = new ArrayList<>();
    }

    public qvtrelation_Relation(
        String isTopLevel        ArrayList<Variable> variables    ) {
        this.isTopLevel = isTopLevel;
        this.variables = variables;
    }

    public String getIstoplevel() {
        return isTopLevel;
    }

    public void setIstoplevel(String isTopLevel) {
        this.isTopLevel = isTopLevel;
    }

    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}