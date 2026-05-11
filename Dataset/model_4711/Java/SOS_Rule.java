





import java.util.List;
import java.util.ArrayList;

public class SOS_Rule  {






    private SOS_Semantics sos_semantics;




    private SOS_Conclusion sos_conclusion;




    private SOS_PremisseList sos_premisselist;




    private List<Variable> variables;


    public SOS_Rule(
    ) {
        this.variables = new ArrayList<>();
    }

    public SOS_Rule(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public SOS_Semantics getSos_semantics() {
        return sos_semantics;
    }

    public void setSos_semantics(SOS_Semantics sos_semantics) {
        this.sos_semantics = sos_semantics;
    }
    public SOS_Conclusion getSos_conclusion() {
        return sos_conclusion;
    }

    public void setSos_conclusion(SOS_Conclusion sos_conclusion) {
        this.sos_conclusion = sos_conclusion;
    }
    public SOS_PremisseList getSos_premisselist() {
        return sos_premisselist;
    }

    public void setSos_premisselist(SOS_PremisseList sos_premisselist) {
        this.sos_premisselist = sos_premisselist;
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}