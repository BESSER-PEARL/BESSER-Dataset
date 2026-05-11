





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_seff_pc_SetVariableAction extends AbstractInternalControlFlowAction {






    private List<VariableUsage> variableusages;


    public pcm_pc_seff_pc_SetVariableAction(
    ) {
        super(
        );
        this.variableusages = new ArrayList<>();
    }

    public pcm_pc_seff_pc_SetVariableAction(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
    }


    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }

}