





import java.util.List;
import java.util.ArrayList;

public class express_core_AlgorithmScope extends LocalScope {






    private List<Variable> variables;




    private List<CommonElement> commonelements;


    public express_core_AlgorithmScope(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
        this.commonelements = new ArrayList<>();
    }

    public express_core_AlgorithmScope(
        ArrayList<Variable> variables,        ArrayList<CommonElement> commonelements    ) {
        this.variables = variables;
        this.commonelements = commonelements;
    }


    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }
    public List<CommonElement> getCommonelements() {
        return commonelements;
    }

    public void addCommonelement(Commonelement commonelement) {
        this.commonelements.add(commonelement);
    }

}