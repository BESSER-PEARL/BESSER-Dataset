





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_SynchronisationPoint  {






    private List<VariableUsage> variableusages;


    public pcm_seff_SynchronisationPoint(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_seff_SynchronisationPoint(
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