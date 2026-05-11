





import java.util.List;
import java.util.ArrayList;

public class SOS_adtmm_ADT  {

    private String name;





    private List<Variable> variables;


    public SOS_adtmm_ADT(
        String name    ) {
        this.name = name;
        this.variables = new ArrayList<>();
    }

    public SOS_adtmm_ADT(
        String name        ArrayList<Variable> variables    ) {
        this.name = name;
        this.variables = variables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}