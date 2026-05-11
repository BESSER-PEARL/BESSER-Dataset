





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_seff_av_pc_CallAction  {






    private List<VariableUsage> variableusages;


    public pcm_av_pc_seff_av_pc_CallAction(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_av_pc_seff_av_pc_CallAction(
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